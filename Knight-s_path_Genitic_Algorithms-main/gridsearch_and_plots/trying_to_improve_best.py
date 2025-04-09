from matplotlib import pyplot as plt
from algorithm.algorithm import GA
from base.population import create_population, evaluate_population
from operators.selection_algorithms import *
from operators.crossovers import *
from operators.mutators import *
from utils.utils import get_elite
from data.data_for_visualization import *


best_scores = []
np.random.seed(0)
seed = np.random.randint(0, 20)
# plotting the best parameter combination
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
                    seed=seed)
    best_scores.append(max(fitness))
plt.plot(best_scores, label = "Best")
best_scores = []

# plotting the best parameter combination but with the new mutator
for data in datasets:
    _, fitness = GA(initializer=create_population(10),
                    evaluator=evaluate_population(values=data),
                    selector=tournament_selection(10),
                    crossover=position_based_crossover,
                    mutator=two_opt_mutation,
                    pop_size=75,
                    n_gens=200,
                    p_xo=0.9,
                    p_m=0.25,
                    elitism=False,
                    elite_func=get_elite(n_elite=1),
                    seed=seed)
    best_scores.append(max(fitness))
plt.plot(best_scores, label = "New mutator", alpha = 0.6)
best_scores = []

# plotting the best parameter combination but with the new crossover
for data in datasets:
    _, fitness = GA(initializer=create_population(10),
                    evaluator=evaluate_population(values=data),
                    selector=tournament_selection(10),
                    crossover=scx,
                    mutator=swap_mutation,
                    pop_size=75,
                    n_gens=200,
                    p_xo=0.9,
                    p_m=0.25,
                    elitism=False,
                    elite_func=get_elite(n_elite=1),
                    seed=seed)
    best_scores.append(max(fitness))
plt.plot(best_scores, label = "New crossover", alpha = 0.4)
best_scores = []

# plotting the best parameter combination but with the new mutator and crossover
for data in datasets:
    _, fitness = GA(initializer=create_population(10),
                    evaluator=evaluate_population(values=data),
                    selector=tournament_selection(10),
                    crossover=scx,
                    mutator=two_opt_mutation,
                    pop_size=75,
                    n_gens=200,
                    p_xo=0.9,
                    p_m=0.25,
                    elitism=False,
                    elite_func=get_elite(n_elite=1),
                    seed=seed)
    best_scores.append(max(fitness))
plt.plot(best_scores, label = "New mutator and crossover", alpha = 0.2)

plt.legend()
plt.show()
