from cah import *

distance = dict()
distance[frozenset({frozenset({'A'}), frozenset({'B'})})] = 1
distance[frozenset({frozenset({'A'}), frozenset({'C'})})] = 2
distance[frozenset({frozenset({'A'}), frozenset({'D'})})] = 1
distance[frozenset({frozenset({'B'}), frozenset({'C'})})] = 1.5
distance[frozenset({frozenset({'B'}), frozenset({'D'})})] = 1
distance[frozenset({frozenset({'C'}), frozenset({'D'})})] = 2

print(cah(distance))
