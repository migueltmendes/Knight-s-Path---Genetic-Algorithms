import random
from data.datafunc import generate_matrix

# create a datasets list with 15 different datasets all with different ranges
datasets = []
for i in range(15):
    random.seed(i)
    datasets.append(generate_matrix(random.randint(-100, -10), random.randint(10, 10000), positive_ratio= random.uniform(0.75, 0.95), seed = i))






