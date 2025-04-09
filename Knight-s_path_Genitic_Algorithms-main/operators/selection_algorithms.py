import random
import numpy as np


def tournament_selection(ts):
    """
    Subset of individuals is randomly selected from the population, and the fittest individual among them is chosen as
    a parent for the next generation.

    :param ts: tournament size (integer)

    :return: function that return the best individual in the tournament
    """
    def inner_tournament(population, fitnesses):
        """
        Chooses the fittest individual among all to be a parent for the next generation.

        :param population: list of lists that represents the population
        :param fitnesses: list that has the fitness of all individuals in the population

        :return: the best individual in the tournament
        """
        # randomly selecting ts number of individuals from the population
        # or, more specifically choosing the individuals from the pop, via their index
        pool = random.choices([i for i in range(len(population))], k=ts)

        # getting the fitnesses of the individuals of a given index
        pool_fits = [fitnesses[i] for i in pool]

        # finding out where in the pool fits the best fitness is
        best = np.argmax(pool_fits)

        # return the individual from the population whose index is the same as the index
        # in pool of the individual who was best in pool fits
        return population[pool[best]]

    return inner_tournament


# Define a function for roulette wheel selection
def roulette_wheel_selection(pop, fitnesses):
    """
    Perform Roulette Wheel Selection to choose individuals from the population based on their fitness scores.

    :param pop: list of lists that represents the population
    :param fitnesses: list that has the fitness of all individuals in the population

    :return: random individual based on fitness
    """
    fit_absolute_val = [abs(fitness) for fitness in fitnesses]
    # Calculate the total fitness of the population
    total_fitness = sum(fit_absolute_val)

    # Create a function that takes the cumulative sum of fitnesses
    cumulative_fitness = []
    cumulative_sum = 0
    for i in range(len(pop)):
        cumulative_sum += fit_absolute_val[i]
        cumulative_fitness.append(cumulative_sum / total_fitness)

    # Generate a random number to select an individual
    random_number = random.random()

    # Find the individual whose cumulative fitness is higher than the random number
    # This ensures that the probability of each being chosen is related to its fitness
    for i, cumulative_value in enumerate(cumulative_fitness):
        if random_number <= cumulative_value:
            return pop[i]


def rank_selection(population, fitnesses):
    """
    Sorts based on individuals' fitness ranks rather than their actual fitness values, with higher-ranking individuals
    having a higher probability of being selected as parents for the next generation.

    :param population: list of lists that represents the population
    :param fitnesses: list that has the fitness of all individuals in the population

    :return: random individual based on rank
    """
    # Sort the population by fitness values
    pop_with_fit = list(zip(population, fitnesses))
    population_sorted = sorted(pop_with_fit, key=lambda x: x[1])  # orders from the smallest fitness to the biggest

    # Create ranks based on sorted fitness
    ranks = list(range(1, len(population_sorted) + 1))
    total_ranks = sum(ranks)

    # Calculate the selection probability based on rank
    probabilities = [rank / total_ranks for rank in ranks]

    # Create a cumulative sum of the probabilities to be easier to see who wins
    cumulative_probabilities = []
    cumulative_sum = 0
    for probability in probabilities:
        cumulative_sum += probability
        cumulative_probabilities.append(cumulative_sum)

    # Generate a random number to select an individual
    random_number = random.random()

    # Find the first individual that has a cumulative probability bigger the random number
    for i, cumulative_value in enumerate(cumulative_probabilities):
        if random_number <= cumulative_value:
            return population_sorted[i][0]


def random_selection(pop, fitness):
    """
    Selects individuals at random

    :param pop: list of lists that represents the population
    :param fitness: list that has the fitness of all individuals in the population

    :return: random individual
    """
    # Randomly select one individual from the population
    return random.choice(pop)
