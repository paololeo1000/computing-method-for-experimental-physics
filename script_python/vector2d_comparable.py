import math

class Vector2d:
    """ Class representing a Vector2d """
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __abs__(self):
        # We need this for __eq__
        return math.sqrt(self.x**2 + self.y**2)

    def __eq__(self, other):
        # Implement the '==' operator
        return ((self.x, self.y) == (other.x, other.y))

    def __ge__(self, other):
        # Implement the '>=' operator
        return abs(self) >= abs(other)

    def __lt__(self, other):
        # Implement the '<' operator
        return abs(self) < abs(other)

    def __repr__(self):
        # We define __repr__ for showing the results nicely
        class_name = type(self).__name__
        return ('{}({}, {})'.format(class_name, self.x, self.y))

v, z = Vector2d(3., -1.), Vector2d(3., 1.)
print(v >= z, v == z, v < z)
# This works even if we don't define the __gt__ method explicitly
print(v > z)

vector_list = [Vector2d(3., -1.), Vector2d(-5., 1.), Vector2d(3., 0.)]
print(vector_list)
# This make the following line work we need to implement either __ge__ and __lt
# or __gt__ and __le__ (we need a complementary pair of operator)
vector_list.sort()
print(vector_list)
# Note: we got the full power of timsort for free! Nice :)