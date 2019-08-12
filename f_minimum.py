def f_minimum(dictionnary, tree_set):
    minimum = -1
    key = ()
    for x in tree_set:
        for y in tree_set:
            if x != y:
                if type(x) == tuple:
                    if type(y) == tuple:
                        for x_son in x:
                            for y_son in y:
                                if (dictionnary[frozenset({x_son, y_son})][1] == 0) and (minimum == -1 or dictionnary[frozenset({x_son, y_son})][0] < minimum):
                                    minimum = dictionnary[frozenset({x_son, y_son})][0]
                                    key = frozenset({x, y})
                    else:
                        for x_son in x:
                            if (dictionnary[frozenset({x_son, y})][1] == 0) and (
                                    minimum == -1 or dictionnary[frozenset({x_son, y})][0] < minimum):
                                minimum = dictionnary[frozenset({x_son, y})][0]
                                key = frozenset({x, y})
                else:
                    if type(y) == tuple:
                        for y_son in y:
                            if (dictionnary[frozenset({x, y_son})][1] == 0) and (minimum == -1 or dictionnary[frozenset({x, y_son})][0] < minimum):
                                minimum = dictionnary[frozenset({x, y_son})][0]
                                key = frozenset({x, y})
                    else:
                        if (dictionnary[frozenset({x, y})][1] == 0) and (
                                minimum == -1 or dictionnary[frozenset({x, y})][0] < minimum):
                            minimum = dictionnary[frozenset({x, y})][0]
                            key = frozenset({x, y})
    return key
