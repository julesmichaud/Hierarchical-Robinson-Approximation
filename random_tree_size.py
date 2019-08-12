from the_algorithm import *
from update_weighted_mean import *
from f_minimum import *
from random import randrange


def random_tree(size, dissimilarity_possibilities):
    dissimilarity = {}
    for first_element in range(size):
        for second_element in range(size):
            if first_element != second_element:
                dissimilarity[
                    frozenset({frozenset({str(first_element)}), frozenset({str(second_element)})})] = \
                    randrange(1, dissimilarity_possibilities)
    return the_algorithm(dissimilarity, f_minimum, update_weighted_mean)


def tree_size(tree):
    max_size = 0
    if len(tree) == 1:
        return 0
    else:
        for i in tree:
            size = tree_size(i) + 1
            if size > max_size:
                max_size = size
        return max_size


def mean_tree_size(number_of_elements, size, dissimilarity_possibilities):
    sum = 0
    for i in range(number_of_elements):
        print(i)
        tree = random_tree(size, dissimilarity_possibilities)
        sum += tree_size(tree)
    mean = sum / number_of_elements
    return mean

# Étant donné que l'on rencontre souvent le problème lié à l'assemblage de 2 Q-nodes avec des dissimilarités qui ne sont
# pas de Robinson, il est idifficile d'effectuer un grand nombre d'essais sans tomber sur une erreur.
# Malgré cela, après maintes essais voilà ce que j'ai pu recueillir :
# - 100 / 5 / 10 : 1,44



