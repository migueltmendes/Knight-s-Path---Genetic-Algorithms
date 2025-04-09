import random
import numpy as np


def cycle_crossover(parent1, parent2):
    """
    Combines two parent solutions by exchanging information based on cycles within their permutation representations

    :param parent1: one individual from the population
    :param parent2: another individual from the population

    :return: Two childs obtained by crossing over the parents
    """
    # Initialize offspring with None values
    n = len(parent1)
    offspring1 = [None] * n
    offspring2 = [None] * n

    def find_cycle(start_index, p1, p2):  # auxiliary function to cycle crossover
        """
        Identifies a cycle within the permutation representations of two parent solutions

        :param start_index: index from where the cycle is supposed to begin
        :param p1: parent1
        :param p2: parent2

        :return: list with the indexes where the values will remain the same as the parents
        """
        cycle = []
        index = start_index
        while True:
            cycle.append(index)
            # Find the index of the element from p2 in p1
            index = p1.index(p2[index])
            if index == start_index:
                break
        return cycle

    # Create a cycle starting from index 1 (since the start and end are fixed as 1)
    cycle1 = find_cycle(1, parent1, parent2)

    # Fill the cycle for offspring1 and offspring2
    for index in cycle1:
        offspring1[index] = parent1[index]
        offspring2[index] = parent2[index]

    # Fill the remaining positions with elements from the other parent
    for i in range(1, n - 1):
        if offspring1[i] is None:
            offspring1[i] = parent2[i]
        if offspring2[i] is None:
            offspring2[i] = parent1[i]

    # Ensure the start and end are 1
    offspring1[0], offspring1[-1] = 1, 1
    offspring2[0], offspring2[-1] = 1, 1

    return offspring1, offspring2


def alternating_position_crossover(parent1, parent2):
    """
    Applies Alternating Position Crossover (APX) to two parent permutations
    with the constraint that the solutions start and end with a specific value.

    :param parent1: one individual from the population
    :param parent2: another individual from the population

    :return: Two childs obtained by crossing over the parents
    """

    n = len(parent1)

    # Initialize two offspring
    offspring1 = [0] * n
    offspring2 = [0] * n

    # Initialize used genes for each offspring
    used_genes1 = set()
    used_genes2 = set()

    # Set the unique start and end
    offspring1[0], offspring1[-1] = 1, 1
    offspring2[0], offspring2[-1] = 1, 1
    used_genes1.add(1)
    used_genes2.add(1)

    # Indices for alternating from parents
    parent1_index = 1
    parent2_index = 1

    # Fill the offspring by alternating between parents
    for i in range(1, n - 1):
        # Alternate between parents for offspring1
        if i % 2 == 0:
            while parent1[parent1_index] in used_genes1:
                parent1_index += 1
            offspring1[i] = parent1[parent1_index]
            used_genes1.add(parent1[parent1_index])
        else:
            while parent2[parent2_index] in used_genes1:
                parent2_index += 1
            offspring1[i] = parent2[parent2_index]
            used_genes1.add(parent2[parent2_index])

        # Alternate between parents for offspring2
        if i % 2 != 0:
            while parent1[parent1_index] in used_genes2:
                parent1_index += 1
            offspring2[i] = parent1[parent1_index]
            used_genes2.add(parent1[parent1_index])
        else:
            while parent2[parent2_index] in used_genes2:
                parent2_index += 1
            offspring2[i] = parent2[parent2_index]
            used_genes2.add(parent2[parent2_index])

    return offspring1, offspring2


def partial_mapped_crossover(parent1, parent2):
    """
    Combines two parent solutions by preserving partially mapped segments

    :param parent1: one individual from the population
    :param parent2: another individual from the population

    :return: Two childs obtained by crossing over the parents
    """
    n = len(parent1)

    # Initialize offspring with None values
    offspring1 = [None] * n
    offspring2 = [None] * n

    # Select random crossover points
    pt1, pt2 = sorted(random.sample(range(1, n), 2))

    # Copy the segment from pt1 to pt2
    offspring1[pt1:pt2] = parent1[pt1:pt2]
    offspring2[pt1:pt2] = parent2[pt1:pt2]

    # Create mappings based on the copied segments
    mapping1 = {parent1[i]: parent2[i] for i in range(pt1, pt2)}
    mapping2 = {parent2[i]: parent1[i] for i in range(pt1, pt2)}

    # Fill in the gaps in the offspring
    def fill_offspring(offspring, mapping, parent):
        """
        Fill the offspring chromosome using the given mapping and parent chromosome.

        :param offspring: The offspring chromosome to be filled.
        :param mapping: A dictionary containing mappings from genes in the parent chromosome to their corresponding
        genes in the offspring chromosome.
        :param parent: The parent chromosome providing the genes for filling the offspring.

        :return The offspring chromosome is filled in place.
        """
        # Fill from left to right to maintain mapping
        for i in range(n):
            if i < pt1 or i >= pt2:
                gene = parent[i]
                # Resolve the mapping to find the appropriate gene
                while gene in mapping:
                    gene = mapping[gene]
                offspring[i] = gene

    # Fill the remaining genes for offspring1 and offspring2
    fill_offspring(offspring1, mapping1, parent2)
    fill_offspring(offspring2, mapping2, parent1)

    return offspring1, offspring2


def position_based_crossover(parent1, parent2):
    """
    Combines two parent solutions by randomly selecting positions from both parents

    :param parent1: one individual from the population
    :param parent2: another individual from the population

    :return: Two childs obtained by crossing over the parents
    """
    n = len(parent1) - 2

    # Generate a random subset of positions (excluding first/last position)
    subset_size = random.randint(1, n)
    positions = random.sample(range(1, n + 1), subset_size)

    # Function to create offspring by using given positions from parent1
    def create_offspring(primary, secondary, positions):
        """
            Create an offspring chromosome by combining cities from the primary and secondary parents.

            :param primary: The chromosome of the primary parent.
            :param secondary: The chromosome of the secondary parent.
            :param positions: A list of positions to be filled with cities from the primary parent.

            :return offspring chromosome created by combining places from the primary and secondary parents.
        """
        # Start with fixed start and end
        offspring = [1]

        # Fill in selected positions with cities from the primary parent
        for pos in sorted(positions):
            offspring.append(primary[pos])

        # Complete the tour with remaining cities from the secondary parent that are not already in the offspring
        remaining = [place for place in secondary if place not in offspring]

        offspring.extend(remaining)
        offspring.append(1)

        return offspring

    # Create two offspring using different primary/secondary roles
    offspring1 = create_offspring(parent1, parent2, positions)
    offspring2 = create_offspring(parent2, parent1, positions)

    return offspring1, offspring2


def scx(parent1, parent2):
    """
    Generates two offsprings where the next place in the individual is chosen based on the order in the parents,
    avoiding repetitions

    :param parent1: one individual from the population
    :param parent2: another individual from the population

    :return:  Two offsprings obtained by crossing over the parents
    """
    def next_place(current, p1, p2, offspring):
        """
        Determines the next place to add to the offspring during the crossover.
        It selects the next place from the current place based on the order in both parents,
        ensuring the place is not already included in the offspring

        :param current: Current place
        :param p1: parent1
        :param p2: parent2
        :param offspring: current state of the offspring

        :return:  The next place to add to the offspring
        """
        idx1 = p1.index(current)
        idx2 = p2.index(current)

        next1 = p1[(idx1 + 1) % (len(p1) - 1)]
        next2 = p2[(idx2 + 1) % (len(p2) - 1)]

        # Choose the next place that isn't already in the offspring
        if next1 in offspring:
            return next2
        if next2 in offspring:
            return next1
        # Prefer next1 if both are valid choices
        return np.random.choice([next1, next2])

    def generate_offspring(start_parent, other_parent):
        """
        Generates an offspring tour using Sequential Constructive Crossover (SCX)

        :param start_parent: starting parent
        :param other_parent: the other parent

        :return: generated offspring
        """
        offspring = [1]
        current_place = 1

        while len(offspring) < len(parent1) - 1:
            next_place_chosen = next_place(current_place, start_parent, other_parent, offspring)
            offspring.append(next_place_chosen)
            current_place = next_place_chosen

        offspring.append(1)  # End with city 1
        return offspring

    offspring1 = generate_offspring(parent1, parent2)
    offspring2 = generate_offspring(parent2, parent1)

    return offspring1, offspring2