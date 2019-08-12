def update_set(tree_set, tree_1, tree_2, new_tree):
    tree_set.remove(tree_1)
    tree_set.remove(tree_2)
    tree_set.add(new_tree)
    return tree_set


def update_size(size, tree_1, tree_2, new_tree):
    size[new_tree] = size[tree_1] + size[tree_2]
    return size


def update_dissimilarity_total(dissimilarity, tree_set, update_dissimilarity, tree_1, tree_2, new_tree, size):
    dissimilarity = update_dissimilarity(dissimilarity, tree_set, tree_1, tree_2, new_tree, size)
    for x in dissimilarity.keys():
        if tree_1 in x or tree_2 in x:
            dissimilarity[x][1] = 1
    if type(new_tree) == tuple:
        for x in tree_set:
            if x != tree_1 and x != tree_2:
                if type(x) == frozenset:
                    if x != new_tree[0]:
                        dissimilarity[frozenset({x, new_tree[0]})][1] = 0
                    if x != new_tree[-1]:
                        dissimilarity[frozenset({x, new_tree[-1]})][1] = 0
                else:
                    if x != new_tree:
                        dissimilarity[frozenset({x[0], new_tree[0]})][1] = 0
                        dissimilarity[frozenset({x[0], new_tree[-1]})][1] = 0
                        dissimilarity[frozenset({x[-1], new_tree[0]})][1] = 0
                        dissimilarity[frozenset({x[-1], new_tree[-1]})][1] = 0
    for x in tree_1:
        for y in tree_2:
            if type(x) != str and type(y) != str:
                dissimilarity[frozenset({x, y})][1] = 1
            if type(x) == str and type(y) != str:
                dissimilarity[frozenset({frozenset({x}), y})][1] = 1
            if type(x) != str and type(y) == str:
                dissimilarity[frozenset({x, frozenset({y})})][1] = 1
            if type(x) == str and type(y) == str:
                dissimilarity[frozenset({frozenset({x}), frozenset({y})})][1] = 1
    return dissimilarity


def updates(tree_1, tree_2, new_tree, size, tree_set, dissimilarity, update_dissimilarity):
    size = update_size(size, tree_1, tree_2, new_tree)
    dissimilarity = update_dissimilarity_total(dissimilarity, tree_set, update_dissimilarity, tree_1, tree_2, new_tree,
                                               size)
    tree_set = update_set(tree_set, tree_1, tree_2, new_tree)
    return tree_set, size, dissimilarity
