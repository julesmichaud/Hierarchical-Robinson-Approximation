EPSILON = 1e-09


def verification_frozenset_1(frozenset_1, frozenset_2, tree_set, dissimilarity):
    for x in tree_set:
        if x != frozenset_1 and x != frozenset_2 and type(x) != tuple and abs(
                dissimilarity[frozenset({frozenset_1, x})][0] - dissimilarity[frozenset({frozenset_2, x})][0]) > EPSILON:
            return True
    return False


def verification_frozenset_2(frozenset_1, frozenset_2, dissimilarity, diameter):
    if (dissimilarity[frozenset({frozenset_1, frozenset_2})][0] - diameter[frozenset_1]) > EPSILON and (
            dissimilarity[frozenset({frozenset_1, frozenset_2})][0] - diameter[frozenset_2]) > EPSILON:
        return True
    return False


def verification_frozenset_3(frozenset_1, frozenset_2, dissimilarity, diameter):
    if abs(dissimilarity[frozenset({frozenset_1, frozenset_2})][0] - diameter[frozenset_1]) <= EPSILON and abs(
            dissimilarity[frozenset({frozenset_1, frozenset_2})][0] - diameter[frozenset_2]) <= EPSILON:
        return True
    return False


def verification_frozenset_4(frozenset_1, frozenset_2, dissimilarity, diameter):
    if abs(dissimilarity[frozenset({frozenset_1, frozenset_2})][0] - diameter[frozenset_1]) <= EPSILON < (
            dissimilarity[frozenset({frozenset_1, frozenset_2})][0] - diameter[frozenset_2]):
        return True
    return False


def verification_frozenset_5(frozenset_1, frozenset_2, dissimilarity, diameter):
    if abs(dissimilarity[frozenset({frozenset_1, frozenset_2})][0] - diameter[frozenset_2]) <= EPSILON < (
            dissimilarity[frozenset({frozenset_1, frozenset_2})][0] - diameter[frozenset_1]):
        return True
    return False


def verification_frozenset_tuple_1(frozenset_1, tuple_1, dissimilarity):
    if dissimilarity[frozenset({frozenset_1, tuple_1[-1]})][0] - dissimilarity[frozenset({frozenset_1, tuple_1[0]})][0] > EPSILON:
        return True
    return False


def verification_frozenset_tuple_2(frozenset_1, tuple_1, dissimilarity):
    if dissimilarity[frozenset({frozenset_1, tuple_1[0]})][0] - dissimilarity[frozenset({frozenset_1, tuple_1[-1]})][0] > EPSILON:
        return True
    return False


def verification_frozenset_tuple_3(frozenset_1, tuple_1, dissimilarity):
    if abs(dissimilarity[frozenset({frozenset_1, tuple_1[0]})][0] - dissimilarity[
        frozenset({frozenset_1, tuple_1[-1]})][0]) <= EPSILON:
        return True
    return False


def verification_frozenset_tuple_3_1(frozenset_1, tuple_1, tree_set, dissimilarity):
    for x in tree_set:
        if x != frozenset_1 and x != tuple_1 and type(x) != tuple and abs(
                dissimilarity[frozenset({x, tuple_1[0]})][0] - dissimilarity[frozenset({x, frozenset_1})][0]) > EPSILON:
            return True
    return False


def verification_tuple_1(tuple_1, tuple_2, dissimilarity):
    if abs(dissimilarity[frozenset({tuple_1[0], tuple_2[0]})][0] - dissimilarity[
        frozenset({tuple_1[0], tuple_2[-1]})][0]) <= EPSILON and abs(
        dissimilarity[frozenset({tuple_1[0], tuple_2[-1]})][0] - dissimilarity[
            frozenset({tuple_1[-1], tuple_2[0]})][0]) <= EPSILON and abs(
        dissimilarity[frozenset({tuple_1[-1], tuple_2[0]})][0] - dissimilarity[frozenset({tuple_1[-1], tuple_2[-1]})][0]) <= EPSILON:
        return True
    return False


def verification_tuple_1_1(tuple_1, tuple_2, tree_set, dissimilarity):
    for x in tree_set:
        if x != tuple_1 and x != tuple_2 and type(x) != tuple and abs(
                dissimilarity[frozenset({x, tuple_2[0]})][0] - dissimilarity[frozenset({x, tuple_1[0]})][0]) > EPSILON:
            return True
    return False


def verification_tuple_2(tuple_1, tuple_2, dissimilarity):
    if abs(dissimilarity[frozenset({tuple_1[0], tuple_2[0]})][0] - dissimilarity[
        frozenset({tuple_1[0], tuple_2[-1]})][0]) <= EPSILON and abs(
        dissimilarity[frozenset({tuple_1[-1], tuple_2[0]})][0] - dissimilarity[frozenset({tuple_1[-1], tuple_2[-1]})][0]) <= EPSILON < \
            dissimilarity[frozenset({tuple_1[0], tuple_2[-1]})][0] - dissimilarity[frozenset({tuple_1[-1], tuple_2[0]})][0]:
        return True
    return False


def verification_tuple_3(tuple_1, tuple_2, dissimilarity):
    if abs(dissimilarity[frozenset({tuple_1[0], tuple_2[0]})][0] - dissimilarity[
        frozenset({tuple_1[-1], tuple_2[0]})][0]) <= EPSILON and abs(
        dissimilarity[frozenset({tuple_1[0], tuple_2[-1]})][0] - dissimilarity[frozenset({tuple_1[-1], tuple_2[-1]})][0]) <= EPSILON < \
            dissimilarity[frozenset({tuple_1[-1], tuple_2[0]})][0] - dissimilarity[frozenset({tuple_1[0], tuple_2[-1]})][0]:
        return True
    return False


def verification_tuple_4(tuple_1, tuple_2, dissimilarity):
    if abs(dissimilarity[frozenset({tuple_1[0], tuple_2[0]})][0] - dissimilarity[
        frozenset({tuple_1[0], tuple_2[-1]})][0]) <= EPSILON and abs(
        dissimilarity[frozenset({tuple_1[-1], tuple_2[0]})][0] - dissimilarity[frozenset({tuple_1[-1], tuple_2[-1]})][0]) <= EPSILON < \
            dissimilarity[frozenset({tuple_1[-1], tuple_2[0]})][0] - dissimilarity[frozenset({tuple_1[0], tuple_2[-1]})][0]:
        return True
    return False


def verification_tuple_5(tuple_1, tuple_2, dissimilarity):
    if abs(dissimilarity[frozenset({tuple_1[0], tuple_2[0]})][0] - dissimilarity[
        frozenset({tuple_1[-1], tuple_2[0]})][0]) <= EPSILON and abs(
        dissimilarity[frozenset({tuple_1[0], tuple_2[-1]})][0] - dissimilarity[frozenset({tuple_1[-1], tuple_2[-1]})][0]) <= EPSILON < \
            dissimilarity[frozenset({tuple_1[0], tuple_2[-1]})][0] - dissimilarity[frozenset({tuple_1[-1], tuple_2[0]})][0]:
        return True
    return False


def verification_tuple_6(tuple_1, tuple_2, dissimilarity):
    if dissimilarity[frozenset({tuple_1[0], tuple_2[-1]})][0] - dissimilarity[frozenset({tuple_1[-1], tuple_2[0]})][0] > EPSILON:
        return True
    return False


def verification_tuple_7(tuple_1, tuple_2, dissimilarity):
    if dissimilarity[frozenset({tuple_1[-1], tuple_2[0]})][0] - dissimilarity[frozenset({tuple_1[0], tuple_2[-1]})][0] > EPSILON:
        return True
    return False
