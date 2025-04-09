# from Base.Individual import *
import csv
import random
import numpy as np
from base.population import *
from copy import deepcopy


def GA(initializer, evaluator, selector, pop_size, crossover, mutator, n_gens, p_xo, p_m, elite_func, verbose=False,
       log_path=None, elitism=True, seed=0):
    """
    Creates a genetic algorithm that will give the best solution.

    :param initializer: function that creates the population
    :param evaluator: function that evaluates the population
    :param selector: function that selects individuals for crossover and mutation
    :param pop_size: size of the population
    :param crossover: function for individuals' crossover
    :param mutator: function for individual's mutation
    :param n_gens: number of generations
    :param p_xo: probability of crossover
    :param p_m: probability of mutation
    :param elite_func: function that returns the n best individuals out of a population
    :param verbose: True if prints throughout the code are to be used, False if not
    :param log_path: path to the file where the results should be stored
    :param elitism: True if you want to keep the n best individuals in the next pop, False if not
    :param seed: seed to set for np.random and random

    :return: population: returns the last population created in the algorithm
    - pop_fit: returns the fitness of the last population created in the algorithm
    """
    # set the seed
    random.seed(seed)
    np.random.seed(seed)

    # check if elite_func exists
    if elite_func is None:
        raise Exception("Error must insert a elite function")

    # Initializing the gen 0 population
    population = initializer(pop_size)

    # Evaluating the current population
    pop_fit = evaluator(population)

    for gen in range(n_gens):

        # Create offspring population
        offspring = []

        # While offspring population is not full
        while len(offspring) < pop_size:
            # Selecting the parents
            p1, p2 = selector(population, pop_fit), selector(population, pop_fit)

            # Choosing between xover and reproduction
            if random.random() < p_xo:
                # do xover
                o1, o2 = crossover(p1, p2)
            else:
                # do reproduction
                o1, o2 = deepcopy(p1), deepcopy(p2)

            o1, o2 = mutator(o1, p_m), mutator(o2, p_m)

            offspring.extend([o1, o2])

        while len(offspring) > pop_size:
            offspring.pop()

        # If elitism, make sure the elite population is inserted into the next generation
        if elitism:
            elite, best_fit = elite_func(population, pop_fit)
            offspring[-len(elite):] = elite  # adding the elite, unchanged into the offspring population

        # Replacing population by the offsprings
        population = offspring

        # Evaluating the current population
        pop_fit = evaluator(population)

        new_elite, new_fit = elite_func(population, pop_fit)
        if verbose:
            print(f"    {gen}      |       {new_fit}       ")
            print("-" * 32)

        if log_path is not None:
            with open(log_path, "a", newline='') as file:
                write = csv.writer(file)
                write.writerow([seed, gen, new_fit, new_elite])

    return population, pop_fit
