"""
CS210 W23
Author: Jose Renteria

Practice passing a function as an argument using Map
Also observing usage of Map

Map function takes a function and an iterable as input:

            Map(function*, iterable)

and returns an object that can be iterated over. (AKA an ITERABLE TYPE)

The function is applied to each element of the iterable, and the result is
returned as a new iterable containing the results.
"""
import unittest


def square(x):
    return x ** 2


squared_numbers = list(map(square, [1, 2, 3, 4]))
print(squared_numbers)


def vector_dilate(vector: list, scalar: int):
    """
    A vector dilation is a type of linear transformation that scales a vector
    by a scalar factor. Given a vector v in a vector space and a scalar s, the
    dilation of v by s is a new vector v' s.t. v' = s * v

    vector_dilate([1, 0, 0], 3)
    3

    """
    # TODO


class test_case(unittest.TestCase):
    def test_dilate_two(self):
        vector = [1, 2, 3]
        scalar = 2
        expected = [2, 4, 6]
        result = vector_dilate(vector, scalar)
        self.assertEqual(result, expected)

    def test_dilate_zero(self):
        vector = [1, 2, 3]
        scalar = 0
        expected = [0, 0, 0]
        result = vector_dilate(vector, scalar)
        self.assertEqual(result, expected)

    def test_dilate_negative(self):
        vector = [1, 2, 3]
        scalar = -1
        expected = [-1, -2, -3]
        result = vector_dilate(vector, scalar)
        self.assertEqual(result, expected)

    def test_dilate_empty(self):
        vector = []
        scalar = 2
        expected = []
        result = vector_dilate(vector, scalar)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
