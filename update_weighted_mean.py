def update_weighted_mean(dissimilarity, tree_set, tree_1, tree_2, new_tree, size):
    for x in new_tree:
        if type(x) == tuple:
            dissimilarity = new_dissimilarity_tuple(dissimilarity, tree_set, x, size)
    if type(new_tree) == frozenset:
        dissimilarity = new_dissimilarity_frozenset(dissimilarity, tree_set, tree_1, tree_2, new_tree, size)
    return dissimilarity


def new_dissimilarity_frozenset(dissimilarity, tree_set, tree_1, tree_2, new_tree, size):
    for x in tree_set:
        if x != tree_1 and x != tree_2:
            if type(x) == frozenset:
                dissimilarity[frozenset({x, new_tree})] = [
                    (dissimilarity[frozenset({tree_1, x})][0] * size[tree_1] +
                     dissimilarity[frozenset({tree_2, x})][0] * size[tree_2]) / size[
                        new_tree], 0]
            if type(x) == tuple:
                for i in range(len(x)):
                    dissimilarity[frozenset({x[i], new_tree})] = [
                        (dissimilarity[frozenset({tree_1, x[i]})][0] * size[tree_1] +
                         dissimilarity[frozenset({tree_2, x[i]})][0] * size[tree_2]) / size[
                            new_tree], 0]
    return dissimilarity


def new_dissimilarity_tuple(dissimilarity, tree_set, tuple_1, size):
    for x in tree_set:
        if x != tuple_1:
            if type(x) == frozenset:
                dissimilarity[frozenset({x, tuple_1})] = [
                    (dissimilarity[frozenset({x, tuple_1[0]})][0] * size[tuple_1[0]] +
                     dissimilarity[frozenset({x, tuple_1[-1]})][0] * size[
                         tuple_1[-1]]) / (size[tuple_1[0]] + size[tuple_1[-1]]), 0]
            else:
                for i in range(len(x)):
                    if x[i] == tuple_1:
                        return dissimilarity
                for j in range(len(x)):
                    dissimilarity[frozenset({x[i], tuple_1})] = [
                        (dissimilarity[frozenset({x[i], tuple_1[0]})][0] * size[tuple_1[0]] +
                         dissimilarity[frozenset({x[i], tuple_1[-1]})][0] * size[
                             tuple_1[-1]]) / (size[tuple_1[0]] + size[tuple_1[-1]]), 0]
    return dissimilarity
