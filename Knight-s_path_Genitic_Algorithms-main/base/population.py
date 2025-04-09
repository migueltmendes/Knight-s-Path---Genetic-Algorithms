from base.individual import *


def create_population(individual_size):
    """
    Creates a population

    :param individual_size: size of the individuals

    :return: function that generates population
    """
    def generate_pop(pop_size):
        """
        Generates population

        :param pop_size: size of the population

        :return: population in the form of a list of lists
        """
        return [generate_solution(individual_size)() for _ in range(pop_size)]

    return generate_pop


def evaluate_population(values):
    """
    Evaluates the population

    :param values: list of lists with the points gained from going from a place to another

    :return: function that evaluates the population
    """
    def pop_eval(population):
        """
        Evaluates the population

        :param population: list of list that represents the population

        :return: list of lists that contain the fitness of each individual in the population
        """
        # Getting the individual evaluating function according to the problem
        evaluate_ind = get_fitness(values)

        # Evaluating each solution in the population
        return [evaluate_ind(ind) for ind in population]

    return pop_eval
