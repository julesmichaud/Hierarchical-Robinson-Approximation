from total_assembly import *
from initial_conditions import *
from updates import *


def find_tree(tree_set, dissimilarity, f):
    key = f(dissimilarity, tree_set)
    key = list(key)
    tree_1 = key[0]
    tree_2 = key[1]
    for x in tree_set:
        if type(x) == tuple:
            if tree_1 in x:
                tree_1 = x
            if tree_2 in x:
                tree_2 = x
    return tree_1, tree_2


def the_algorithm(dictionnary, f, update_dissimilarity):
    # dictionnary est le dictionnaire qui regroupe les dissimilarités entre tous les éléments
    # f est une fonction qui choisit à partir des dissimilarités quels arbres fusionner à chaque itération, et qui
    #   renvoie la clé correspondant à ces deux arbres dans le dictionnaire des dissimilarités
    # update_distance est une fonction qui calcule les nouvelles distances entre chaques objets du nouvel arbre après
    #   chaque itération
    tree_set, diameter, dissimilarity, size = initial_configuration(dictionnary)
    while len(tree_set) > 1:
        tree_1, tree_2 = find_tree(tree_set, dissimilarity, f)
        new_tree, diameter = final_assembly(tree_1, tree_2, tree_set, dissimilarity, diameter)
        tree_set, size, dissimilarity = updates(tree_1, tree_2, new_tree, size, tree_set, dissimilarity,
                                                update_dissimilarity)
    return list(tree_set)[0]

# def create_distance():
#     print('to finish, please input stop')
#     distance = {}
#     while -1 < 1:
#         object_1 = input("first object")
#         if object_1 != 'stop':
#             object_2 = input("second object")
#             if object_2 != 'stop':
#                 distances = input('distance between objects')
#                 if distances != 'stop':
#                     distance[frozenset({frozenset({str(object_1)}), frozenset({str(object_2)})})] = float(distances)
#                 else:
#                     return distance
#             else:
#                 return distance
#         else:
#             return distance
