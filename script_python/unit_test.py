import unittest

def square(x):
    return x**2

class TestSquare(unittest.TestCase):

    def test(self):
        self.assertAlmostEqual(square(2.), 4.)


if __name__ == '__main__':
    unittest.main()

    
