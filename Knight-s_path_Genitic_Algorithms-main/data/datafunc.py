import random

def generate_matrix(minimum, maximum, positive_ratio=0.9, seed = 0):
    """
    Generates a matrix (list of lists) that is to be used as a dataset as it has the points gained or lost from a place
    to place

    :param minimum: lowest value possible for the dataset (must be negative)
    :param maximum: highest value possible for the dataset (must be positive)
    :param positive_ratio: ratio of positive values of the dataset
    :param seed: seed to be set for numpy.random and random

    :return: list of lists that has the points gained or lost from a place
    """
    #set the seed
    random.seed(seed)
    matrix = [[0] * 10 for _ in range(10)]  # Initialize a 10x10 matrix with zeros

    # Generate positive and negative numbers
    num_positive = int(positive_ratio * 90)
    num_negative = 90 - num_positive
    positive_numbers = [random.randint(1, maximum) for _ in range(num_positive)]
    negative_numbers = [random.randint(minimum, 0) for _ in range(num_negative)]

    # Shuffle positive and negative numbers
    matrix_values = positive_numbers + negative_numbers
    random.shuffle(matrix_values)

    # Fill the matrix with positive and negative numbers
    for i in range(10):
        for j in range(10):
            if i == j:  # Diagonal elements should be zeros
                continue
            else:
                matrix[i][j] = matrix_values.pop()

    # Ensure the number in the third line, second column is at least 3.2% less than the minimum of all other positive
    # numbers
    positive_values = [num for row in matrix for num in row if num > 0]
    if positive_values:
        min_positive = min(positive_values)
        threshold = min_positive - (min_positive * 0.032)
        while matrix[2][1] >= threshold:
            matrix[2][1] -= 1

    return matrix