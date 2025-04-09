from tqdm import trange

from algorithm.algorithm import GA
from base.population import create_population, evaluate_population
from operators.selection_algorithms import *
from operators.crossovers import *
from operators.mutators import *
from utils.utils import get_elite
from data.data_for_visualization import *


data_to_input = datasets[0] # needs data to be inputted


# function based parameters
initializer = create_population(10)
evaluator = evaluate_population(values=data_to_input)
selector = tournament_selection(10)
xover = position_based_crossover
mutator = swap_mutation
elite_func = get_elite(n_elite=1)

# evolution based parameters
pop_size = 75
n_gens = 200
p_xover = 0.9
p_m = 0.25

for seed in trange(15):

    GA(initializer=initializer,
       evaluator=evaluator,
       selector=selector,
       crossover=xover,
       mutator=mutator,
       pop_size=pop_size,
       n_gens=n_gens,
       p_xo=p_xover,
       p_m=p_m,
       verbose=False,
       log_path="log/test_log.csv",
       elitism=False,
       elite_func=elite_func,
       seed= seed)