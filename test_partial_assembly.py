from partial_assembly import *


def test_assembly_frozenset_A1():
    assert assembly_frozenset_A1(frozenset({frozenset({1}), frozenset({2})}),
                                 frozenset({frozenset({3}), frozenset({4})})) == frozenset(
        {frozenset({frozenset({1}), frozenset({2})}), frozenset({frozenset({3}), frozenset({4})})})
    assert assembly_frozenset_A1(frozenset({(1,), (2,)}), frozenset({(3,), (4,)})) == frozenset(
        {frozenset({(1,), (2,)}), frozenset({(3,), (4,)})})


def test_assembly_frozenset_A2():
    assert assembly_frozenset_A2(frozenset({frozenset({1}), frozenset({2})}),
                                 frozenset({frozenset({3}), frozenset({4})})) == frozenset(
        {frozenset({1}), frozenset({2}), frozenset({3}), frozenset({4})})
    assert assembly_frozenset_A2(frozenset({(1,), (2,)}), frozenset({(3,), (4,)})) == frozenset(
        {(1,), (2,), (3,), (4,)})


def test_assembly_frozenset_A3():
    assert assembly_frozenset_A3(frozenset({frozenset({1}), frozenset({2})}),
                                 frozenset({frozenset({3}), frozenset({4})})) == frozenset(
        {frozenset({1}), frozenset({2}), frozenset({frozenset({3}), frozenset({4})})})
    assert assembly_frozenset_A3(frozenset({(1,), (2,)}), frozenset({(3,), (4,)})) == frozenset(
        {(1,), (2,), frozenset({(3,), (4,)})})


def test_assembly_frozenset_B():
    assert assembly_frozenset_B(frozenset({frozenset({1}), frozenset({2})}),
                                frozenset({frozenset({3}), frozenset({4})})) == (
               frozenset({frozenset({1}), frozenset({2})}), frozenset({frozenset({3}), frozenset({4})}))
    assert assembly_frozenset_B(frozenset({(1,), (2,)}), frozenset({(3,), (4,)})) == (
        frozenset({(1,), (2,)}), frozenset({(3,), (4,)}))


def test_assembly_frozenset_tuple_A():
    assert assembly_frozenset_tuple_A(frozenset({frozenset({1})}),
                                      (frozenset({2}), frozenset({3}), frozenset({4}))) == (
               frozenset({frozenset({1})}), frozenset({2}), frozenset({3}), frozenset({4}))
    assert assembly_frozenset_tuple_A(frozenset({(1,)}), ((2,), (3,), (4,))) == (
        frozenset({(1,)}), (2,), (3,), (4,))


def test_assembly_frozenset_tuple_B():
    assert assembly_frozenset_tuple_B(frozenset({frozenset({1})}),
                                      (frozenset({2}), frozenset({3}), frozenset({4}))) == (
               frozenset({2}), frozenset({3}), frozenset({4}),
               frozenset({frozenset({1})}))
    assert assembly_frozenset_tuple_B(frozenset({(1,)}), ((2,), (3,), (4,))) == ((2,), (3,), (4,), frozenset({(1,)}))


def test_assembly_frozenset_tuple_C1():
    assert assembly_frozenset_tuple_C1(frozenset({frozenset({1})}),
                                       (frozenset({2}), frozenset({3}), frozenset({4}))) == frozenset({
        frozenset({frozenset({1})}), (frozenset({2}), frozenset({3}), frozenset({4}))})
    assert assembly_frozenset_tuple_C1(frozenset({(1,)}), ((2,), (3,), (4,))) == frozenset(
        {frozenset({(1,)}), ((2,), (3,), (4,))})


def test_assembly_frozenset_tuple_C2():
    assert assembly_frozenset_tuple_C2(frozenset({frozenset({1})}),
                                       (frozenset({2}), frozenset({3}), frozenset({4}))) == (
               frozenset({frozenset({1})}), (frozenset({2}), frozenset({3}), frozenset({4})))
    assert assembly_frozenset_tuple_C2(frozenset({(1,)}), ((2,), (3,), (4,))) == (frozenset({(1,)}), ((2,), (3,), (4,)))


def test_assembly_tuple_A():
    assert assembly_tuple_A((frozenset({1}), frozenset({2})), (frozenset({3}), frozenset({4}))) == (
        frozenset({1}), frozenset({2}), frozenset({3}), frozenset({4}))
    assert assembly_tuple_A(((1,), (2,)), ((3,), (4,))) == ((1,), (2,), (3,), (4,))


def test_assembly_tuple_B1():
    assert assembly_tuple_B1((frozenset({1}), frozenset({2})), (frozenset({3}), frozenset({4}))) == (
        frozenset({1}), frozenset({2}), (frozenset({3}), frozenset({4})))
    assert assembly_tuple_B1(((1,), (2,)), ((3,), (4,))) == ((1,), (2,), ((3,), (4,)))


def test_assembly_tuple_B2():
    assert assembly_tuple_B2((frozenset({1}), frozenset({2})), (frozenset({3}), frozenset({4}))) == (
        (frozenset({3}), frozenset({4})), frozenset({1}), frozenset({2}))
    assert assembly_tuple_B2(((1,), (2,)), ((3,), (4,))) == (((3,), (4,)), (1,), (2,))


def test_assembly_tuple_C1():
    assert assembly_tuple_C1((frozenset({1}), frozenset({2})), (frozenset({3}), frozenset({4}))) == frozenset({
        (frozenset({1}), frozenset({2})), (frozenset({3}), frozenset({4}))})
    assert assembly_tuple_C1(((1,), (2,)), ((3,), (4,))) == frozenset({((1,), (2,)), ((3,), (4,))})


def test_assembly_tuple_C2():
    assert assembly_tuple_C2((frozenset({1}), frozenset({2})), (frozenset({3}), frozenset({4}))) == (
        (frozenset({1}), frozenset({2})), (frozenset({3}), frozenset({4})))
    assert assembly_tuple_C2(((1,), (2,)), ((3,), (4,))) == (((1,), (2,)), ((3,), (4,)))
