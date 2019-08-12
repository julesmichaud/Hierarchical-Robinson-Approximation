def initial_set(dictionnary):
    tree_set = set()
    for x in dictionnary.keys():
        x = list(x)
        tree_set.add(x[0])
        tree_set.add(x[1])
    return tree_set


def initial_dissimilarity(dictionnary):
    dissimilarity = {}
    for key, value in dictionnary.items():
        dissimilarity[key] = [value, 0]
    return dissimilarity


def initial_diameter(dictionnary):
    diameter = dict()
    for x in dictionnary.keys():
        x = list(x)
        diameter[x[0]] = 0
        diameter[x[1]] = 0
    return diameter


def initial_size(dictionnary):
    size = {}
    for x in dictionnary.keys():
        x = list(x)
        size[x[0]] = 1
        size[x[1]] = 1
    return size


def initial_configuration(dictionnary):
    tree_set = initial_set(dictionnary)
    diameter = initial_diameter(dictionnary)
    dissimilarity = initial_dissimilarity(dictionnary)
    size = initial_size(dictionnary)
    return tree_set, diameter, dissimilarity, size
