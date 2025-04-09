import random


def swap_mutation(ind, p_m):
    """
    Randomly selects two genes within a chromosome and swaps their positions

    :param ind: individual
    :param p_m: probability of mutation

    :return: mutated individual or the original individual if it doesn't happen mutation
    """
    if random.random() < p_m:
        # Randomly select two distinct indices for swapping
        index1, index2 = random.sample(range(1, len(ind) - 1), 2)

        # Swap them
        ind[index1], ind[index2] = ind[index2], ind[index1]

    return ind


def inversion_mutation(ind, p_m):
    """
    Randomly selects a subset of genes within a chromosome and reverses their order

    :param ind: individual
    :param p_m: probability of mutation

    :return: mutated individual or the original individual if it doesn't happen mutation
    """
    if random.random() < p_m:
        # Randomly select two distinct indices to define the inversion range
        index1, index2 = sorted(random.sample(range(1, len(ind) - 1), 2))

        # Invert them
        ind[index1:index2 + 1] = reversed(ind[index1:index2 + 1])

    return ind


def scramble_mutation(ind, p_m):
    """
    Randomly selects a subset of genes within a chromosome and shuffles their positions to introduce diversity

    :param ind: individual
    :param p_m: probability of mutation

    :return: mutated individual or the original individual if it doesn't happen mutation
    """
    if random.random() < p_m:
        # Randomly select two distinct indices to define the scramble range
        index1, index2 = sorted(random.sample(range(1, len(ind) - 1), 2))

        # Extract the subset to be scrambled
        subset = ind[index1:index2 + 1]

        # Shuffle it
        random.shuffle(subset)

        # Reinsert the scrambled subset into the individual
        ind[index1:index2 + 1] = subset

    return ind


def insertion_mutation(ind, p_m):
    """
     Randomly selects a gene and inserts it into a different position within the chromosome

    :param ind: individual
    :param p_m: probability of mutation

    :return: mutated individual or the original individual if it doesn't happen mutation
    """
    if random.random() < p_m:
        # Randomly select a position to remove a city from.
        remove_pos = random.randint(1, len(ind) - 2)

        to_insert = ind[remove_pos]
        remaining = ind[:remove_pos] + ind[remove_pos + 1:]

        # Choose a new position to insert the removed place.
        insert_pos = random.randint(1, len(remaining) - 2)

        ind = remaining[:insert_pos] + [to_insert] + remaining[insert_pos:]

    return ind


def two_opt_mutation(ind, p_m):
    """
    Inverses the path between index 1 and index 2 chosen at random without changing the position of the selected indexes
    only the one of the indexes in the middle. Similar to swap mutator but instead of inverting all only inverses
    between the indexes chosen.

    :param ind: individual
    :param p_m: probability of mutation

    :return: mutated individual or the original individual if it doesn't happen mutation
    """
    if random.random() < p_m:
        # Select two random indices for edges, excluding the first and last elements
        idx1, idx2 = random.sample(range(1, len(ind) - 1), 2)

        # Sort the indices
        idx1, idx2 = sorted([idx1, idx2])
        print(idx1, idx2)

        # Reverse the segment between the selected indices
        ind[idx1+1:idx2] = ind[idx1+1:idx2][::-1]

    return ind
