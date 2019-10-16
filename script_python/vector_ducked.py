import math
from array import array

class Vector:
    """ Class representing a multidimensional vector """
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __len__(self):
        return len(self._components)

    def __iter__(self):
        return iter(self._components)

    def __str__(self):
        return str(tuple(self)) # tuple() accept an iterable

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self)) # tuple comprehension

    def __add__(self, other):
        """ zip returns a sequence of pairs from two iterables """
        return Vector([x + y for x, y in zip(self, other)])

    def __eq__(self, other):
        return (len(self) == len(other)) and \
            (all(a == b for a, b in zip(self, other))) # Efficiency test!


v = Vector([1., 2., 3.])
t = Vector([1., 2., 3., 4.])
z = Vector([1., 2., 5.])
u = Vector([1., 2., 3.])

print(v)
print(abs(v))
print(v == t, v == z, v == u)
print(v + z)
print(v + t)
