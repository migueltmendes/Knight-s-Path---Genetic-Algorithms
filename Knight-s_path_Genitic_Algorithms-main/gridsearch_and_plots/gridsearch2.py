import itertools
import random
import numpy as np
from algorithm.algorithm import GA
from base.population import create_population, evaluate_population
from operators.selection_algorithms import *
from operators.crossovers import *
from operators.mutators import *
from utils.utils import get_elite
from data.datafunc import generate_matrix

# create a datasets list with 5 different datasets with the same range
dataset_grid_search2 = []
for i in range(5):
    random.seed(i)
    dataset_grid_search2.append(generate_matrix(minimum=-10000, maximum=100000, positive_ratio= random.uniform(0.75, 0.95), seed = i))


def evaluate_ga(hyperparameters, dataset, evaluate_population, runs=3):
    """
    Gridsearch that finds out which parameters yield the best results

    :param hyperparameters: dictionary which keys are the GA's parameters and the values are a list of its possible values
    :param dataset: list of all the different datasets to be used
    :param evaluate_population: function that will be used to evaluate the population
    :param runs: number of times that each dataset should run for the same GA's parameters

    :return:
    - best_params: parameters that got the best result in the form of a dictionary
    - top_score: fitness gotten by the best parameters
    - three_of_the_best_best: list with the three best parameters combination
    """
    # Create all combinations of hyperparameters
    results = {}
    dataset_score = []
    keys = list(hyperparameters.keys())
    param_combinations = list(itertools.product(*[hyperparameters[key] for key in keys]))

    top_score = -float("inf")
    best_params = None


    # Iterate over each combination of hyperparameters
    for param_set in param_combinations:
        param_dict = dict(zip(keys, param_set))
        best_scores = []
        print("Testing:", param_dict)

        # Repeat the GA simulation for a given number of runs
        for data in dataset:
            for seed in range(runs):
                # Set seed
                random.seed(seed)
                np.random.seed(seed)
                # Execute the GA simulation with the given hyperparameters
                _, fitness = GA(
                    pop_size=param_dict["pop_size"],
                    p_m=param_dict["p_m"],
                    p_xo=param_dict["p_xo"],
                    n_gens=param_dict["n_gens"],
                    selector=param_dict["selector"],
                    mutator=param_dict["mutator"],
                    elitism=param_dict["elitism"],
                    elite_func=param_dict["elite_func"],
                    crossover=param_dict["crossover"],
                    evaluator=evaluate_population(values=data),
                    initializer=param_dict["initializer"],
                    seed=seed  # Pass the unique seed
                )

                # Add the best score for this run to the list
                best_scores.append(max(fitness))


            # Calculate the median best score for parameter combination for the dataset
            dataset_score.append(np.median(best_scores))
            best_scores = []

        # Sum the medians of all datasets
        score = sum(dataset_score)
        print(score)
        dataset_score = []

        # If this combination has the best average score, update best_params
        if score > top_score:
            top_score = score
            best_params = param_dict.copy()

        results[tuple(sorted(param_dict.items()))] = score

    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

    # Get 3 of the best key-value pairs
    three_of_the_best_best = sorted_results[:3]

    return best_params, top_score, three_of_the_best_best


hyperparameters = {

    "pop_size": [75, 100],
    "p_m": [0.15, 0.25],
    "p_xo": [0.8, 0.9],
    "n_gens": [150, 200],
    "selector": [roulette_wheel_selection, random_selection, rank_selection, tournament_selection(2), tournament_selection(10)],
    "mutator": [swap_mutation, inversion_mutation, scramble_mutation, insertion_mutation],
    "elitism": [True, False],
    "elite_func": [get_elite(1), get_elite(2), get_elite(3)],
    "crossover": [cycle_crossover, alternating_position_crossover, partial_mapped_crossover, position_based_crossover],
    "initializer": [create_population(10)]
}
# Perform the grid search to determine the best hyperparameters
best_params, best_avg_score, three_of_the_best = evaluate_ga(hyperparameters, dataset= dataset_grid_search2, evaluate_population= evaluate_population)


print("Best Parameters:", best_params)
print("Best Average Score:", best_avg_score)
print("Another of the best parameters combination and its score:", three_of_the_best)