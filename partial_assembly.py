def assembly_frozenset_A1(frozenset_1, frozenset_2):
    return frozenset({frozenset_1, frozenset_2})


def assembly_frozenset_A2(frozenset_1, frozenset_2):
    new_tree = set()
    for x in frozenset_1:
        new_tree.add(x)
    for y in frozenset_2:
        new_tree.add(y)
    return frozenset(new_tree)


def assembly_frozenset_A3(frozenset_1, frozenset_2):
    new_tree = set()
    for x in frozenset_1:
        new_tree.add(x)
    new_tree.add(frozenset_2)
    return frozenset(new_tree)


def assembly_frozenset_B(frozenset_1, frozenset_2):
    return frozenset_1, frozenset_2


def assembly_frozenset_tuple_A(frozenset_1, tuple_1):
    new_tree = (frozenset_1,)
    for i in range(len(tuple_1)):
        new_tree += (tuple_1[i],)
    return new_tree


def assembly_frozenset_tuple_B(frozenset_1, tuple_1):
    new_tree = ()
    for i in range(len(tuple_1)):
        new_tree += (tuple_1[i],)
    new_tree += (frozenset_1,)
    return new_tree


def assembly_frozenset_tuple_C1(frozenset_1, tuple_1):
    return frozenset({frozenset_1, tuple_1})


def assembly_frozenset_tuple_C2(frozenset_1, tuple_1):
    return frozenset_1, tuple_1


def assembly_tuple_A(tuple_1, tuple_2):
    new_tree = ()
    for i in range(len(tuple_1)):
        new_tree += (tuple_1[i],)
    for j in range(len(tuple_2)):
        new_tree += (tuple_2[j],)
    return new_tree


def assembly_tuple_B1(tuple_1, tuple_2):
    new_tree = ()
    for i in range(len(tuple_1)):
        new_tree += (tuple_1[i],)
    new_tree += (tuple_2,)
    return new_tree


def assembly_tuple_B2(tuple_1, tuple_2):
    new_tree = (tuple_2,)
    for i in range(len(tuple_1)):
        new_tree += (tuple_1[i],)
    return new_tree


def assembly_tuple_C1(tuple_1, tuple_2):
    return frozenset({tuple_1,tuple_2})


def assembly_tuple_C2(tuple_1, tuple_2):
    return tuple_1, tuple_2