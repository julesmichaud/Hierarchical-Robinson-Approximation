from partial_assembly import *

EPSILON = 1e-09


def verification_1(frozenset_1, frozenset_2, distance, diameter):
    if (distance[frozenset({frozenset_1, frozenset_2})] - diameter[frozenset_1]) > EPSILON and (
            distance[frozenset({frozenset_1, frozenset_2})] - diameter[frozenset_2]) > EPSILON:
        return True
    return False


def verification_2(frozenset_1, frozenset_2, distance, diameter):
    if abs(distance[frozenset({frozenset_1, frozenset_2})] - diameter[frozenset_1]) <= EPSILON and abs(
            distance[frozenset({frozenset_1, frozenset_2})] - diameter[frozenset_2]) <= EPSILON:
        return True
    return False


def verification_3(frozenset_1, frozenset_2, distance, diameter):
    if abs(distance[frozenset({frozenset_1, frozenset_2})] - diameter[frozenset_1]) <= EPSILON < (
            distance[frozenset({frozenset_1, frozenset_2})] - diameter[frozenset_2]):
        return True
    return False


def verification_4(frozenset_1, frozenset_2, distance, diameter):
    if abs(distance[frozenset({frozenset_1, frozenset_2})] - diameter[frozenset_2]) <= EPSILON < (
            distance[frozenset({frozenset_1, frozenset_2})] - diameter[frozenset_1]):
        return True
    return False


def assembly_frozenset(frozenset_1, frozenset_2, distance, diameter):
    if verification_1(frozenset_1, frozenset_2, distance, diameter):
        new_tree = assembly_frozenset_A1(frozenset_1, frozenset_2)
        diameter[new_tree] = distance[frozenset({frozenset_1, frozenset_2})]
        return new_tree, diameter
    if verification_2(frozenset_1, frozenset_2, distance, diameter):
        new_tree = assembly_frozenset_A2(frozenset_1, frozenset_2)
        diameter[new_tree] = diameter[frozenset_1]
        return new_tree, diameter
    if verification_3(frozenset_1, frozenset_2, distance, diameter):
        new_tree = assembly_frozenset_A3(frozenset_1, frozenset_2)
        diameter[new_tree] = diameter[frozenset_1]
        return new_tree, diameter
    if verification_4(frozenset_1, frozenset_2, distance, diameter):
        new_tree = assembly_frozenset_A3(frozenset_2, frozenset_1)
        diameter[new_tree] = diameter[frozenset_2]
        return new_tree, diameter


def find_tree(distance):
    key = distance_min(distance)
    key = list(key)
    tree_1 = key[0]
    tree_2 = key[1]
    return tree_1, tree_2


def update_distance(tree_set, distance, tree_1, tree_2, new_tree):
    for x in tree_set:
        if x != tree_1 and x != tree_2:
            distance[frozenset({new_tree, x})] = (distance[frozenset({tree_1, x})] + distance[
                frozenset({tree_2, x})]) / 2
            del distance[frozenset({tree_1, x})]
            del distance[frozenset({tree_2, x})]
    del distance[frozenset({tree_1, tree_2})]
    return distance


def update_set(tree_set, tree_1, tree_2, new_tree):
    tree_set.remove(tree_1)
    tree_set.remove(tree_2)
    tree_set.add(new_tree)
    return tree_set


def distance_min(dictionnary):
    minimum = -1
    key = ()
    for x in dictionnary.keys():
        if minimum == -1 or dictionnary[x] < minimum:
            minimum = dictionnary[x]
            key = x
    return key


def initial_set(dictionnary):
    tree_set = set()
    for x in dictionnary.keys():
        x = list(x)
        tree_set.add(x[0])
        tree_set.add(x[1])
    return tree_set


def initial_diameter(dictionnary):
    diameter = dict()
    for x in dictionnary.keys():
        x = list(x)
        diameter[x[0]] = 0
        diameter[x[1]] = 0
    return diameter


def initial_conditions(distance):
    tree_set = initial_set(distance)
    diameter = initial_diameter(distance)
    return tree_set, diameter


def cah(distance):
    tree_set, diameter = initial_conditions(distance)
    while len(tree_set) > 1:
        tree_1, tree_2 = find_tree(distance)
        new_tree, diameter = assembly_frozenset(tree_1, tree_2, distance, diameter)
        distance = update_distance(tree_set, distance, tree_1, tree_2, new_tree)
        tree_set = update_set(tree_set, tree_1, tree_2, new_tree)
    return list(tree_set)[0]


def create_distance():
    print('to finish, please input stop')
    distance = {}
    while -1 < 1:
        object_1 = input("first object")
        if object_1 != 'stop':
            object_2 = input("second object")
            if object_2 != 'stop':
                distances = input('distance between objects')
                if distances != 'stop':
                    distance[frozenset({frozenset({str(object_1)}), frozenset({str(object_2)})})] = float(distances)
                else:
                    return distance
            else:
                return distance
        else:
            return distance
