import numpy as np


def get_elite(n_elite):
    """
    Gets the n_elite best elements in the population

    :param n_elite: number of the best elements wanted to get from the population

    :return: the n best elements from the population
    """
    # returns the elite and the elite fitness
    def elites(population, fitnesses):
        """
        Gets the n_elite best elements in the population

        :param population: list of lists representing the population
        :param fitnesses: list with the fitness of each individual of the population

        :return: n best individuals of the population
        """
        bests_i = np.argsort(fitnesses)[-n_elite:]

        return [population[i] for i in bests_i], [fitnesses[i] for i in bests_i]

    return elites
