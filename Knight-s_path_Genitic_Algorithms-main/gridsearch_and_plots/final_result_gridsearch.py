import numpy as np
from matplotlib import pyplot as plt

from algorithm.algorithm import GA
from base.population import create_population, evaluate_population
from data.data_for_visualization import datasets
from operators.crossovers import position_based_crossover
from operators.mutators import swap_mutation
from operators.selection_algorithms import tournament_selection
from utils.utils import get_elite

np.random.seed(10)
best_scores = []
# plot the best parameter combination in 15 different datasets
for data in datasets:
    _, fitness = GA(initializer=create_population(10),
                    evaluator=evaluate_population(values=data),
                    selector=tournament_selection(10),
                    crossover=position_based_crossover,
                    mutator=swap_mutation,
                    pop_size=75,
                    n_gens=200,
                    p_xo=0.9,
                    p_m=0.25,
                    elitism=False,
                    elite_func=get_elite(n_elite=1),
                    seed=np.random.randint(0,20))
    best_scores.append(max(fitness))
plt.plot(best_scores)
plt.show()
best_scores = []
# plot the best parameter combination in 15 different seeds
n_data = np.random.randint(0, 15)
for i in range(15):
    _, fitness = GA(initializer=create_population(10),
                    evaluator=evaluate_population(values=datasets[n_data]),
                    selector=tournament_selection(10),
                    crossover=position_based_crossover,
                    mutator=swap_mutation,
                    pop_size=75,
                    n_gens=200,
                    p_xo=0.9,
                    p_m=0.25,
                    elitism=False,
                    elite_func=get_elite(n_elite=1),
                    seed=i)
    best_scores.append(max(fitness))
plt.plot(best_scores)
plt.show()