from the_algorithm import *
from update_weighted_mean import *
from f_minimum import *
from random import randrange

distance = {}
for i in range(5):
    for j in range(5):
        if i != j:
            distance[frozenset({frozenset({str(i)}), frozenset({str(j)})})] = randrange(1,10)

# distance[frozenset({frozenset({'A'}), frozenset({'B'})})] = randrange(1,10)
# distance[frozenset({frozenset({'A'}), frozenset({'C'})})] = randrange(1,10)
# distance[frozenset({frozenset({'A'}), frozenset({'D'})})] = randrange(1,10)
# distance[frozenset({frozenset({'A'}), frozenset({'E'})})] = randrange(1,10)
# distance[frozenset({frozenset({'B'}), frozenset({'C'})})] = randrange(1,10)
# distance[frozenset({frozenset({'B'}), frozenset({'D'})})] = randrange(1,10)
# distance[frozenset({frozenset({'B'}), frozenset({'E'})})] = randrange(1,10)
# distance[frozenset({frozenset({'C'}), frozenset({'D'})})] = randrange(1,10)
# distance[frozenset({frozenset({'C'}), frozenset({'E'})})] = randrange(1,10)
# distance[frozenset({frozenset({'D'}), frozenset({'E'})})] = randrange(1,10)
print(distance)
print(the_algorithm(distance, f_minimum, update_weighted_mean))

# problème de NoneType
# distance = {}
# distance[frozenset({frozenset({'A'}), frozenset({'B'})})] = 8
# distance[frozenset({frozenset({'A'}), frozenset({'C'})})] = 2
# distance[frozenset({frozenset({'A'}), frozenset({'D'})})] = 6
# distance[frozenset({frozenset({'A'}), frozenset({'E'})})] = 8
# distance[frozenset({frozenset({'B'}), frozenset({'C'})})] = 1
# distance[frozenset({frozenset({'B'}), frozenset({'D'})})] = 7
# distance[frozenset({frozenset({'B'}), frozenset({'E'})})] = 4
# distance[frozenset({frozenset({'C'}), frozenset({'D'})})] = 2
# distance[frozenset({frozenset({'C'}), frozenset({'E'})})] = 7
# distance[frozenset({frozenset({'D'}), frozenset({'E'})})] = 2
#
# print(the_algorithm(distance, f_minimum, update_weighted_mean))
