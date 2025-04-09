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

# best parameter combination from the first gridsearch
for data in datasets:
    _, fitness = GA(initializer=create_population(10),
                    evaluator=evaluate_population(values=data),
                    selector=tournament_selection(2),
                    crossover=position_based_crossover,
                    mutator=scramble_mutation,
                    pop_size=50,
                    n_gens=150,
                    p_xo=0.9,
                    p_m=0.15,
                    elitism=True,
                    elite_func=get_elite(n_elite=3),
                    seed=seed)
    best_scores.append(max(fitness))
plt.plot(best_scores, label = "Algorithm gridsearch1")
best_scores = []

# best parameter combination from the second gridsearch
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
plt.plot(best_scores, label = "Algorithm gridsearch2")
plt.legend()
plt.show()
