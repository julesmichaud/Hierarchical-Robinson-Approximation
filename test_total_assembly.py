from total_assembly import *


def test_assembly_frozenset_tuple():
    tree_1 = frozenset({frozenset({1}), frozenset({2}), frozenset({3})})
    tree_2 = (frozenset({4}), frozenset({5}), frozenset({6}))
    tree_set = {tree_1, tree_2}

    diameter = {}
    distance = {}
    distance[frozenset({tree_1, tree_2[0]})] = [2, 0]
    distance[frozenset({tree_1, tree_2[1]})] = [1.5, 0]
    distance[frozenset({tree_1, tree_2[2]})] = [1, 0]
    assert assembly_frozenset_tuple(tree_1, tree_2, tree_set, distance, diameter) == ((
                                                                                          frozenset({4}),
                                                                                          frozenset({5}),
                                                                                          frozenset({6}),
                                                                                          frozenset({frozenset({1}),
                                                                                                     frozenset({2}),
                                                                                                     frozenset({3})})),
                                                                                      {})

    diameter = {}
    distance = {}
    distance[frozenset({tree_1, tree_2[0]})] = [1, 0]
    distance[frozenset({tree_1, tree_2[1]})] = [1.5, 0]
    distance[frozenset({tree_1, tree_2[2]})] = [2, 0]
    assert assembly_frozenset_tuple(tree_1, tree_2, tree_set, distance, diameter) == ((
                                                                                          frozenset({frozenset({1}),
                                                                                                     frozenset({2}),
                                                                                                     frozenset({3})}),
                                                                                          frozenset({4}),
                                                                                          frozenset({5}),
                                                                                          frozenset({6})), {})

    diameter = {}
    distance = {}
    distance[frozenset({tree_1, tree_2[0]})] = [1, 0]
    distance[frozenset({tree_1, tree_2[1]})] = [1, 0]
    distance[frozenset({tree_1, tree_2[2]})] = [1, 0]
    assert assembly_frozenset_tuple(tree_1, tree_2, tree_set, distance, diameter) == (frozenset(
        {frozenset({frozenset({1}), frozenset({2}), frozenset({3})}),
         (frozenset({4}), frozenset({5}), frozenset({6}))}), {frozenset(
        {frozenset({frozenset({1}), frozenset({2}), frozenset({3})}),
         (frozenset({4}), frozenset({5}), frozenset({6}))}): 1})

    diameter = {}
    distance = {}
    tree_3 = frozenset({7})
    tree_set.add(tree_3)
    distance[frozenset({tree_1, tree_2[0]})] = [1, 0]
    distance[frozenset({tree_1, tree_2[1]})] = [1, 0]
    distance[frozenset({tree_1, tree_2[2]})] = [1, 0]
    distance[frozenset({tree_3, tree_1})] = [1.1, 0]
    distance[frozenset({tree_3, tree_2[0]})] = [1.2, 0]
    distance[frozenset({tree_3, tree_2[1]})] = [1.2, 0]
    distance[frozenset({tree_3, tree_2[2]})] = [1.2, 0]
    assert assembly_frozenset_tuple(tree_1, tree_2, tree_set, distance, diameter) == ((
                                                                                          frozenset({frozenset({1}),
                                                                                                     frozenset({2}),
                                                                                                     frozenset({3})}),
                                                                                          (frozenset({4}),
                                                                                           frozenset({5}),
                                                                                           frozenset({6}))), {})


def test_assembly_frozenset():
    tree_1 = frozenset({frozenset({1}), frozenset({2}), frozenset({3})})
    tree_2 = frozenset({frozenset({4}), frozenset({5}), frozenset({6})})
    tree_set = {tree_1, tree_2}

    diameter = {}
    distance = {}
    distance[frozenset({tree_1, tree_2})] = [2, 0]
    diameter[tree_1] = 1
    diameter[tree_2] = 1
    assert assembly_frozenset(tree_1, tree_2, tree_set, distance, diameter) == (frozenset(
        {frozenset({frozenset({1}), frozenset({2}), frozenset({3})}),
         frozenset({frozenset({4}), frozenset({5}), frozenset({6})})}), {frozenset(
        {frozenset({frozenset({1}), frozenset({2}), frozenset({3})}),
         frozenset({frozenset({4}), frozenset({5}), frozenset({6})})}): 2, tree_1: 1, tree_2: 1})

    diameter = {}
    distance = {}
    distance[frozenset({tree_1, tree_2})] = [2, 0]
    diameter[tree_1] = 2
    diameter[tree_2] = 1
    assert assembly_frozenset(tree_1, tree_2, tree_set, distance, diameter) == (frozenset(
        {frozenset({1}), frozenset({2}), frozenset({3}),
         frozenset({frozenset({4}), frozenset({5}), frozenset({6})})}), {frozenset(
        {frozenset({1}), frozenset({2}), frozenset({3}),
         frozenset({frozenset({4}), frozenset({5}), frozenset({6})})}): 2, tree_1: 2, tree_2: 1})

    diameter = {}
    distance = {}
    distance[frozenset({tree_1, tree_2})] = [2, 0]
    diameter[tree_1] = 1
    diameter[tree_2] = 2
    assert assembly_frozenset(tree_1, tree_2, tree_set, distance, diameter) == (frozenset(
        {frozenset({frozenset({1}), frozenset({2}), frozenset({3})}),
         frozenset({4}), frozenset({5}), frozenset({6})}), {frozenset(
        {frozenset({frozenset({1}), frozenset({2}), frozenset({3})}),
         frozenset({4}), frozenset({5}), frozenset({6})}): 2, tree_1: 1, tree_2: 2})

    diameter = {}
    distance = {}
    distance[frozenset({tree_1, tree_2})] = [2,0]
    diameter[tree_1] = 2
    diameter[tree_2] = 2
    assert assembly_frozenset(tree_1, tree_2, tree_set, distance, diameter) == (frozenset(
        {frozenset({1}), frozenset({2}), frozenset({3}),
         frozenset({4}), frozenset({5}), frozenset({6})}), {frozenset(
        {frozenset({1}), frozenset({2}), frozenset({3}),
         frozenset({4}), frozenset({5}), frozenset({6})}): 2, tree_1: 2, tree_2: 2})

    tree_3 = (frozenset({7}))
    tree_set.add(tree_3)
    diameter = {}
    distance = {}
    distance[frozenset({tree_1, tree_2})] = [2, 0]
    distance[frozenset({tree_1, tree_3})] = [4, 0]
    distance[frozenset({tree_2, tree_3})] = [3, 0]
    diameter[tree_1] = 1
    diameter[tree_2] = 1
    assert assembly_frozenset(tree_1, tree_2, tree_set, distance, diameter) == ((frozenset(
        {frozenset({1}), frozenset({2}), frozenset({3})}), frozenset({
        frozenset({4}), frozenset({5}), frozenset({6})})), {tree_1: 1, tree_2: 1})


def test_assembly_tuple():
    tree_1 = (frozenset({1}), frozenset({2}), frozenset({3}))
    tree_2 = (frozenset({4}), frozenset({5}), frozenset({6}))
    tree_set = {tree_1, tree_2}

    diameter = {}
    distance = {}
    distance[frozenset({tree_1[0], tree_2[0]})] = [1, 0]
    distance[frozenset({tree_1[0], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[0], tree_2[2]})] = [3, 0]
    distance[frozenset({tree_1[1], tree_2[0]})] = [4, 0]
    distance[frozenset({tree_1[1], tree_2[1]})] = [5, 0]
    distance[frozenset({tree_1[1], tree_2[2]})] = [6, 0]
    distance[frozenset({tree_1[2], tree_2[0]})] = [7, 0]
    distance[frozenset({tree_1[2], tree_2[1]})] = [8, 0]
    distance[frozenset({tree_1[2], tree_2[2]})] = [9, 0]
    assert assembly_tuple(tree_1, tree_2, tree_set, distance, diameter) == (
        (frozenset({4}), frozenset({5}), frozenset({6}), frozenset({1}), frozenset({2}), frozenset({3})), {})

    diameter = {}
    distance = {}
    distance[frozenset({tree_1[0], tree_2[0]})] = [9, 0]
    distance[frozenset({tree_1[0], tree_2[1]})] = [8, 0]
    distance[frozenset({tree_1[0], tree_2[2]})] = [7, 0]
    distance[frozenset({tree_1[1], tree_2[0]})] = [6, 0]
    distance[frozenset({tree_1[1], tree_2[1]})] = [5, 0]
    distance[frozenset({tree_1[1], tree_2[2]})] = [4, 0]
    distance[frozenset({tree_1[2], tree_2[0]})] = [3, 0]
    distance[frozenset({tree_1[2], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[2], tree_2[2]})] = [1, 0]
    assert assembly_tuple(tree_1, tree_2, tree_set, distance, diameter) == (
        (frozenset({1}), frozenset({2}), frozenset({3}), frozenset({4}), frozenset({5}), frozenset({6})), {})

    diameter = {}
    distance = {}
    distance[frozenset({tree_1[0], tree_2[0]})] = [3, 0]
    distance[frozenset({tree_1[0], tree_2[1]})] = [3, 0]
    distance[frozenset({tree_1[0], tree_2[2]})] = [3, 0]
    distance[frozenset({tree_1[1], tree_2[0]})] = [2, 0]
    distance[frozenset({tree_1[1], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[1], tree_2[2]})] = [2, 0]
    distance[frozenset({tree_1[2], tree_2[0]})] = [1, 0]
    distance[frozenset({tree_1[2], tree_2[1]})] = [1, 0]
    distance[frozenset({tree_1[2], tree_2[2]})] = [1, 0]
    assert assembly_tuple(tree_1, tree_2, tree_set, distance, diameter) == (
        (frozenset({1}), frozenset({2}), frozenset({3}), (frozenset({4}), frozenset({5}), frozenset({6}))), {})

    diameter = {}
    distance = {}
    distance[frozenset({tree_1[0], tree_2[0]})] = [1, 0]
    distance[frozenset({tree_1[0], tree_2[1]})] = [1, 0]
    distance[frozenset({tree_1[0], tree_2[2]})] = [1, 0]
    distance[frozenset({tree_1[1], tree_2[0]})] = [2, 0]
    distance[frozenset({tree_1[1], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[1], tree_2[2]})] = [2, 0]
    distance[frozenset({tree_1[2], tree_2[0]})] = [3, 0]
    distance[frozenset({tree_1[2], tree_2[1]})] = [3, 0]
    distance[frozenset({tree_1[2], tree_2[2]})] = [3, 0]
    assert assembly_tuple(tree_1, tree_2, tree_set, distance, diameter) == (
        ((frozenset({4}), frozenset({5}), frozenset({6})), frozenset({1}), frozenset({2}), frozenset({3})), {})

    diameter = {}
    distance = {}
    distance[frozenset({tree_1[0], tree_2[0]})] = [3, 0]
    distance[frozenset({tree_1[0], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[0], tree_2[2]})] = [1, 0]
    distance[frozenset({tree_1[1], tree_2[0]})] = [3, 0]
    distance[frozenset({tree_1[1], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[1], tree_2[2]})] = [1, 0]
    distance[frozenset({tree_1[2], tree_2[0]})] = [3, 0]
    distance[frozenset({tree_1[2], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[2], tree_2[2]})] = [1, 0]
    assert assembly_tuple(tree_1, tree_2, tree_set, distance, diameter) == (
        (frozenset({4}), frozenset({5}), frozenset({6}), (frozenset({1}), frozenset({2}), frozenset({3}))), {})

    diameter = {}
    distance = {}
    distance[frozenset({tree_1[0], tree_2[0]})] = [1, 0]
    distance[frozenset({tree_1[0], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[0], tree_2[2]})] = [3, 0]
    distance[frozenset({tree_1[1], tree_2[0]})] = [1, 0]
    distance[frozenset({tree_1[1], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[1], tree_2[2]})] = [3, 0]
    distance[frozenset({tree_1[2], tree_2[0]})] = [1, 0]
    distance[frozenset({tree_1[2], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[2], tree_2[2]})] = [3, 0]
    assert assembly_tuple(tree_1, tree_2, tree_set, distance, diameter) == (
        ((frozenset({1}), frozenset({2}), frozenset({3})), frozenset({4}), frozenset({5}), frozenset({6})), {})

    diameter = {}
    distance = {}
    distance[frozenset({tree_1[0], tree_2[0]})] = [2, 0]
    distance[frozenset({tree_1[0], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[0], tree_2[2]})] = [2, 0]
    distance[frozenset({tree_1[1], tree_2[0]})] = [2, 0]
    distance[frozenset({tree_1[1], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[1], tree_2[2]})] = [2, 0]
    distance[frozenset({tree_1[2], tree_2[0]})] = [2, 0]
    distance[frozenset({tree_1[2], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[2], tree_2[2]})] = [2, 0]
    assert assembly_tuple(tree_1, tree_2, tree_set, distance, diameter) == (
        frozenset({(frozenset({1}), frozenset({2}), frozenset({3})), (frozenset({4}), frozenset({5}), frozenset({6}))}),
        {frozenset(
            {(frozenset({1}), frozenset({2}), frozenset({3})), (frozenset({4}), frozenset({5}), frozenset({6}))}): 2})

    tree_3 = (frozenset({7}))
    tree_set.add(tree_3)
    diameter = {}
    distance = {}
    distance[frozenset({tree_1[0], tree_2[0]})] = [2, 0]
    distance[frozenset({tree_1[0], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[0], tree_2[2]})] = [2, 0]
    distance[frozenset({tree_1[1], tree_2[0]})] = [2, 0]
    distance[frozenset({tree_1[1], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[1], tree_2[2]})] = [2, 0]
    distance[frozenset({tree_1[2], tree_2[0]})] = [2, 0]
    distance[frozenset({tree_1[2], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[2], tree_2[2]})] = [2, 0]
    distance[frozenset({tree_3, tree_1[0]})] = [1, 0]
    distance[frozenset({tree_3, tree_2[0]})] = [1.5, 0]
    assert assembly_tuple(tree_1, tree_2, tree_set, distance, diameter) == (
        ((frozenset({1}), frozenset({2}), frozenset({3})), (frozenset({4}), frozenset({5}), frozenset({6}))),
        {})

    tree_3 = (frozenset({7}))
    tree_set.add(tree_3)
    diameter = {}
    distance = {}
    distance[frozenset({tree_1[0], tree_2[0]})] = [2, 0]
    distance[frozenset({tree_1[0], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[0], tree_2[2]})] = [2, 0]
    distance[frozenset({tree_1[1], tree_2[0]})] = [2, 0]
    distance[frozenset({tree_1[1], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[1], tree_2[2]})] = [2, 0]
    distance[frozenset({tree_1[2], tree_2[0]})] = [2, 0]
    distance[frozenset({tree_1[2], tree_2[1]})] = [2, 0]
    distance[frozenset({tree_1[2], tree_2[2]})] = [2, 0]
    distance[frozenset({tree_3, tree_1[0]})] = [1, 0]
    distance[frozenset({tree_3, tree_2[0]})] = [1, 0]
    assert assembly_tuple(tree_1, tree_2, tree_set, distance, diameter) == (
        frozenset({(frozenset({1}), frozenset({2}), frozenset({3})), (frozenset({4}), frozenset({5}), frozenset({6}))}),
        {frozenset(
            {(frozenset({1}), frozenset({2}), frozenset({3})), (frozenset({4}), frozenset({5}), frozenset({6}))}): 2})

