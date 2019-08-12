from partial_assembly import *
from verifications import *


def assembly_frozenset(frozenset_1, frozenset_2, tree_set, dissimilarity, diameter):
    if verification_frozenset_2(frozenset_1, frozenset_2, dissimilarity, diameter):
        if verification_frozenset_1(frozenset_1, frozenset_2, tree_set, dissimilarity):
            new_tree = assembly_frozenset_B(frozenset_1, frozenset_2)
            return new_tree, diameter
        else:
            new_tree = assembly_frozenset_A1(frozenset_1, frozenset_2)
            diameter[new_tree] = dissimilarity[frozenset({frozenset_1, frozenset_2})][0]
            return new_tree, diameter
    if verification_frozenset_3(frozenset_1, frozenset_2, dissimilarity, diameter):
        new_tree = assembly_frozenset_A2(frozenset_1, frozenset_2)
        diameter[new_tree] = diameter[frozenset_1]
        return new_tree, diameter
    if verification_frozenset_4(frozenset_1, frozenset_2, dissimilarity, diameter):
        new_tree = assembly_frozenset_A3(frozenset_1, frozenset_2)
        diameter[new_tree] = diameter[frozenset_1]
        return new_tree, diameter
    if verification_frozenset_5(frozenset_1, frozenset_2, dissimilarity, diameter):
        new_tree = assembly_frozenset_A3(frozenset_2, frozenset_1)
        diameter[new_tree] = diameter[frozenset_2]
        return new_tree, diameter


def assembly_frozenset_tuple(frozenset_1, tuple_1, tree_set, dissimilarity, diameter):
    if verification_frozenset_tuple_1(frozenset_1, tuple_1, dissimilarity):
        new_tree = assembly_frozenset_tuple_A(frozenset_1, tuple_1)
        return new_tree, diameter
    if verification_frozenset_tuple_2(frozenset_1, tuple_1, dissimilarity):
        new_tree = assembly_frozenset_tuple_B(frozenset_1, tuple_1)
        return new_tree, diameter
    if verification_frozenset_tuple_3(frozenset_1, tuple_1, dissimilarity):
        if verification_frozenset_tuple_3_1(frozenset_1, tuple_1, tree_set, dissimilarity):
            new_tree = assembly_frozenset_tuple_C2(frozenset_1, tuple_1)
            return new_tree, diameter
        else:
            new_tree = assembly_frozenset_tuple_C1(frozenset_1, tuple_1)
            diameter[new_tree] = dissimilarity[frozenset({frozenset_1, tuple_1[0]})][0]
            return new_tree, diameter


def assembly_tuple(tuple_1, tuple_2, tree_set, dissimilarity, diameter):
    if verification_tuple_1(tuple_1, tuple_2, dissimilarity):
        if verification_tuple_1_1(tuple_1, tuple_2, tree_set, dissimilarity):
            new_tree = assembly_tuple_C2(tuple_1, tuple_2)
            return new_tree, diameter
        else:
            new_tree = assembly_tuple_C1(tuple_1, tuple_2)
            diameter[new_tree] = dissimilarity[frozenset({tuple_1[0], tuple_2[0]})][0]
            return new_tree, diameter
    if verification_tuple_2(tuple_1, tuple_2, dissimilarity):
        new_tree = assembly_tuple_B1(tuple_1, tuple_2)
        return new_tree, diameter
    if verification_tuple_3(tuple_1, tuple_2, dissimilarity):
        new_tree = assembly_tuple_B1(tuple_2, tuple_1)
        return new_tree, diameter
    if verification_tuple_4(tuple_1, tuple_2, dissimilarity):
        new_tree = assembly_tuple_B2(tuple_1, tuple_2)
        return new_tree, diameter
    if verification_tuple_5(tuple_1, tuple_2, dissimilarity):
        new_tree = assembly_tuple_B2(tuple_2, tuple_1)
        return new_tree, diameter
    if verification_tuple_6(tuple_1, tuple_2, dissimilarity):
        new_tree = assembly_tuple_A(tuple_1, tuple_2)
        return new_tree, diameter
    if verification_tuple_7(tuple_1, tuple_2, dissimilarity):
        new_tree = assembly_tuple_A(tuple_2, tuple_1)
        return new_tree, diameter


def final_assembly(tree_1, tree_2, tree_set, dissimilarity, diameter):
    if type(tree_1) == tuple:
        if type(tree_2) == tuple:
            return assembly_tuple(tree_1, tree_2, tree_set, dissimilarity, diameter)
        if type(tree_2) == frozenset:
            return assembly_frozenset_tuple(tree_2, tree_1, tree_set, dissimilarity, diameter)
    if type(tree_1) == frozenset:
        if type(tree_2) == tuple:
            return assembly_frozenset_tuple(tree_1, tree_2, tree_set, dissimilarity, diameter)
        if type(tree_2) == frozenset:
            return assembly_frozenset(tree_1, tree_2, tree_set, dissimilarity, diameter)
