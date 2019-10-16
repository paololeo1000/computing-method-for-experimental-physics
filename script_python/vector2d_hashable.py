class Vector2d:
    """ Class representing a Vector2d """
    def __init__(self, x, y):
        """ We tell the user that x and y are private """
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        """ Provides read only access to x - since there is no setter """
        return self._x

    @property
    def y(self):
        """ Provides read only access to y - since there is no setter """
        return self._y

    def __eq__(self, other):
        return ((self.x, self.y) == (other.x, other.y))

    def __hash__(self):
        """ As hash value we provide the logical XOR of the hash of the two 
        coordinates """
        return hash(self.x) ^ hash(self.y)

    def __repr__(self):
        # Again we need __repr__ to display the results nicely
        class_name = type(self).__name__
        return('{}({}, {})'.format(class_name, self.x, self.y))


v, t, z = Vector2d(3., -1.), Vector2d(-5., 1.), Vector2d(3., -1.)
# Check the equality
print(v == t, v == z, t == z)
# Check the hash: v and z are equal, so they will have the same hash
print(hash(v), hash(t), hash(z))
# v and t have different hash, so they can be in the same set
print({v, t})
# v and z have the same hash -- only one will be stored in the set!
print({v, z})
