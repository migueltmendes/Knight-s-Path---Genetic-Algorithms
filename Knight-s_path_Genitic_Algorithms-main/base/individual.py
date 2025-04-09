import numpy as np



def generate_solution(n_places):
    """
    Generates an individual

    :param n_places: number of places a player need to visit

    :return: generate_sol: function tha creates the individual for the algorithm
    """
    def generate_sol():
        """
        Generates individual

        :return: individual
        """
        # Create a list with all numbers from 2 to 10
        sol = [i for i in range(2, n_places + 1)]
        # shuffles the previous list so that we get a random one
        np.random.shuffle(sol)
        # Insert the start place and ending place
        sol.insert(0, 1)
        sol.append(1)

        return sol

    return generate_sol


def get_fitness(values):
    """
    Gets the fitness of an individual

    :param values: list of list containing the points gained or lost from going from a place to another

    :return: function that gets the fitness of the individual
    """
    def fitness(sol):
        """
        Calculates the fitness of the solution by checking in the matrix the value from going from one place to the other

        :param sol: individual to be evaluated

        :return: fitness of the individual
        """
        points = []
        # condition number 2 and 3
        if sol[sol.index(5) + 1] == 6 or 8 in sol[:(len(sol)) // 2]:
            return -1  # we chose to return -1 as most values from going from a place to another are positive so the
            # sum of the values will very often be bigger than -1 making these solutions always or almost always the
            # worst one, and can never be considered the best as it will be always at least a path that has the sum
            # of values bigger than -1 (most values from going from a place to another are positive), also cannot be
            # 0 as some functions use cumulative sum and 0 would yield problems in order of probabilities being
            # different from 0

        # condition number 1
        elif sol.index(4) == sol.index(9) + 1:
            for i in range(len(sol) - 2):
                points.append(values[sol[i] - 1][sol[i + 1] - 1])
            return max([sum(points) - values[sol[sol.index(7)]][sol[sol.index(7)] + 1] - values[sol[sol.index(7)]][sol[sol.index(7)] - 1] + values[sol[sol.index(7)] + 1][sol[sol.index(7)] - 1], sum(points)])
        # all other cases
        else:
            for i in range(len(sol) - 1):
                points.append(values[sol[i] - 1][sol[i + 1] - 1])

            return sum(points)

    return fitness
