from the_algorithm import *
from f_minimum import *
from update_weighted_mean import *
from time import *

f = f_minimum
update_dissimilarity = update_weighted_mean


def test_the_algorithm():
    distance = {}
    distance[frozenset({frozenset({'A'}), frozenset({'B'})})] = 1
    distance[frozenset({frozenset({'A'}), frozenset({'C'})})] = 3
    distance[frozenset({frozenset({'A'}), frozenset({'D'})})] = 6
    distance[frozenset({frozenset({'B'}), frozenset({'C'})})] = 2
    distance[frozenset({frozenset({'B'}), frozenset({'D'})})] = 5
    distance[frozenset({frozenset({'C'}), frozenset({'D'})})] = 3
    result = the_algorithm(distance, f, update_dissimilarity)
    assert result == (
        frozenset({'A'}), frozenset({'B'}), frozenset({'C'}), frozenset({'D'})) or result == (
               frozenset({'D'}), frozenset({'C'}), frozenset({'B'}), frozenset({'A'}))

    distance = {}
    distance[frozenset({frozenset({'A'}), frozenset({'B'})})] = 1
    distance[frozenset({frozenset({'A'}), frozenset({'C'})})] = 2
    distance[frozenset({frozenset({'A'}), frozenset({'D'})})] = 3.5
    distance[frozenset({frozenset({'B'}), frozenset({'C'})})] = 2
    distance[frozenset({frozenset({'B'}), frozenset({'D'})})] = 2.5
    distance[frozenset({frozenset({'C'}), frozenset({'D'})})] = 3
    result = the_algorithm(distance, f, update_dissimilarity)
    assert result == frozenset({
        frozenset({'D'}), (frozenset({'C'}), (frozenset({'A'}), frozenset({'B'})))}) or result == frozenset({
        frozenset({'D'}), (frozenset({'C'}), (frozenset({'B'}), frozenset({'A'})))})

    distance = {}
    distance[frozenset({frozenset({'A'}), frozenset({'B'})})] = 1
    distance[frozenset({frozenset({'A'}), frozenset({'C'})})] = 2
    distance[frozenset({frozenset({'A'}), frozenset({'D'})})] = 3.5
    distance[frozenset({frozenset({'B'}), frozenset({'C'})})] = 2
    distance[frozenset({frozenset({'B'}), frozenset({'D'})})] = 2.5
    distance[frozenset({frozenset({'C'}), frozenset({'D'})})] = 3
    distance[frozenset({frozenset({'E'}), frozenset({'A'})})] = 5.5
    distance[frozenset({frozenset({'E'}), frozenset({'B'})})] = 6.5
    distance[frozenset({frozenset({'E'}), frozenset({'C'})})] = 6
    distance[frozenset({frozenset({'E'}), frozenset({'D'})})] = 5
    result = the_algorithm(distance, f, update_dissimilarity)
    assert result == (
        frozenset({'E'}), frozenset({'D'}), (frozenset({'C'}), (frozenset({'A'}), frozenset({'B'})))) or result == (
               frozenset({'E'}), frozenset({'D'}),
               (frozenset({'C'}), (frozenset({'B'}), frozenset({'A'})))) or result == (
               frozenset({'E'}), frozenset({'D'}),
               ((frozenset({'A'}), frozenset({'B'})), frozenset({'C'}))) or result == (
               frozenset({'E'}), frozenset({'D'}), ((frozenset({'B'}), frozenset({'A'})), frozenset({'C'})))

    distance = {}
    distance[frozenset({frozenset({'A'}), frozenset({'B'})})] = 1
    distance[frozenset({frozenset({'A'}), frozenset({'C'})})] = 2
    distance[frozenset({frozenset({'A'}), frozenset({'D'})})] = 3
    distance[frozenset({frozenset({'A'}), frozenset({'E'})})] = 7
    distance[frozenset({frozenset({'B'}), frozenset({'C'})})] = 2
    distance[frozenset({frozenset({'B'}), frozenset({'D'})})] = 3
    distance[frozenset({frozenset({'B'}), frozenset({'E'})})] = 7
    distance[frozenset({frozenset({'C'}), frozenset({'D'})})] = 2.5
    distance[frozenset({frozenset({'C'}), frozenset({'E'})})] = 5.3
    distance[frozenset({frozenset({'D'}), frozenset({'E'})})] = 2.8
    result = the_algorithm(distance, f, update_dissimilarity)
    assert result == (frozenset({frozenset({'A'}), frozenset({'B'})}), frozenset({'C'}), frozenset({'D'}),
                      frozenset({'E'})) or result == (
               frozenset({'E'}), frozenset({'D'}), frozenset({'C'}), frozenset({frozenset({'B'}), frozenset({'A'})}))

    distance = {}
    distance[frozenset({frozenset({'A'}), frozenset({'B'})})] = 1
    distance[frozenset({frozenset({'A'}), frozenset({'C'})})] = 2
    distance[frozenset({frozenset({'A'}), frozenset({'D'})})] = 3
    distance[frozenset({frozenset({'A'}), frozenset({'E'})})] = 2.6
    distance[frozenset({frozenset({'B'}), frozenset({'C'})})] = 2
    distance[frozenset({frozenset({'B'}), frozenset({'D'})})] = 3
    distance[frozenset({frozenset({'B'}), frozenset({'E'})})] = 2.6
    distance[frozenset({frozenset({'C'}), frozenset({'D'})})] = 2.5
    distance[frozenset({frozenset({'C'}), frozenset({'E'})})] = 2.8
    distance[frozenset({frozenset({'D'}), frozenset({'E'})})] = 5.3
    result = the_algorithm(distance, f, update_dissimilarity)
    assert result == (frozenset({'E'}), frozenset({frozenset({'A'}), frozenset({'B'})}), frozenset({'C'}),
                      frozenset({'D'})) or result == (
               frozenset({'D'}), frozenset({'C'}), frozenset({frozenset({'B'}), frozenset({'A'})}), frozenset({'E'}))

    distance = {}
    distance[frozenset({frozenset({'A'}), frozenset({'B'})})] = 1
    distance[frozenset({frozenset({'A'}), frozenset({'C'})})] = 2
    distance[frozenset({frozenset({'A'}), frozenset({'D'})})] = 3
    distance[frozenset({frozenset({'A'}), frozenset({'E'})})] = 4
    distance[frozenset({frozenset({'B'}), frozenset({'C'})})] = 2
    distance[frozenset({frozenset({'B'}), frozenset({'D'})})] = 3
    distance[frozenset({frozenset({'B'}), frozenset({'E'})})] = 4
    distance[frozenset({frozenset({'C'}), frozenset({'D'})})] = 3
    distance[frozenset({frozenset({'C'}), frozenset({'E'})})] = 4
    distance[frozenset({frozenset({'D'}), frozenset({'E'})})] = 4
    result = the_algorithm(distance, f, update_dissimilarity)
    assert result == frozenset({frozenset({'E'}), frozenset(
        {frozenset({'D'}), frozenset({frozenset({'C'}), frozenset({frozenset({'B'}), frozenset({'A'})})})})})

    distance = {}
    distance[frozenset({frozenset({'A'}), frozenset({'B'})})] = 1
    distance[frozenset({frozenset({'A'}), frozenset({'C'})})] = 1
    distance[frozenset({frozenset({'A'}), frozenset({'D'})})] = 1
    distance[frozenset({frozenset({'A'}), frozenset({'E'})})] = 1
    distance[frozenset({frozenset({'B'}), frozenset({'C'})})] = 1
    distance[frozenset({frozenset({'B'}), frozenset({'D'})})] = 1
    distance[frozenset({frozenset({'B'}), frozenset({'E'})})] = 1
    distance[frozenset({frozenset({'C'}), frozenset({'D'})})] = 1
    distance[frozenset({frozenset({'C'}), frozenset({'E'})})] = 1
    distance[frozenset({frozenset({'D'}), frozenset({'E'})})] = 1
    result = the_algorithm(distance, f, update_dissimilarity)
    assert result == frozenset(
        {frozenset({'A'}), frozenset({'B'}), frozenset({'C'}), frozenset({'D'}), frozenset({'E'})})

    distance = {}
    distance[frozenset({frozenset({'A'}), frozenset({'B'})})] = 1
    distance[frozenset({frozenset({'A'}), frozenset({'C'})})] = 3
    distance[frozenset({frozenset({'A'}), frozenset({'D'})})] = 6
    distance[frozenset({frozenset({'A'}), frozenset({'E'})})] = 10
    distance[frozenset({frozenset({'B'}), frozenset({'C'})})] = 2
    distance[frozenset({frozenset({'B'}), frozenset({'D'})})] = 5
    distance[frozenset({frozenset({'B'}), frozenset({'E'})})] = 9
    distance[frozenset({frozenset({'C'}), frozenset({'D'})})] = 3
    distance[frozenset({frozenset({'C'}), frozenset({'E'})})] = 7
    distance[frozenset({frozenset({'D'}), frozenset({'E'})})] = 4
    result = the_algorithm(distance, f, update_dissimilarity)
    assert result == (
    frozenset({'A'}), frozenset({'B'}), frozenset({'C'}), frozenset({'D'}), frozenset({'E'})) or result == (
           frozenset({'E'}), frozenset({'D'}), frozenset({'C'}), frozenset({'B'}), frozenset({'A'}))
