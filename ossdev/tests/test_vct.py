#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ossdev
import math
import unittest
from ossdev import Vector


class VectorTest(unittest.TestCase):
    """Simple vector tests"""

    def __init__(self, *args, **kwargs):
        super(VectorTest, self).__init__(*args, **kwargs)

    def test_add(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        c = a + b

        self.assertEqual(c.get(), [3, 3, 3, 3])

    def test_dot(self):
        a = Vector([1, 2])
        b = Vector([2, -1])
        self.assertEqual(a.dot(b), 0)

    def test_setitem(self):
        a = Vector([0, 1, 2, 3])
        a.__setitem__(1, 5)

        self. assertEqual(a[1], 5)

    def test_cmp(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        c = a.__cmp__(b)

        self.assertEqual(c, 0)

    def test_reversed(self):
        a = Vector([0, 1, 2, 3])
        a = a.__reversed__()

        self.assertEqual(a, [3, 2, 1, 0])

    def test_sub(self):
        a = Vector([0, 1, 2, 3])
        b = a.__sub__(a)

        self.assertEqual(b, [0, 0, 0, 0])

    def test_mul(self):
        a = Vector([0, 1, 2, 3])
        b = a.__mul__(2)
        c = a.__mul__(b)

        self.assertEqual(b.d, [0, 2, 4, 6])
        self.assertEqual(c.d, [0, 2, 8, 18])

    def test_xor(self):
        a = Vector([0, 1, 2, 3])
        b = a.__xor__(2)
        c = Vector([0 ^ 2, 1 ^ 2, 2 ^ 2, 3 ^ 2])

        self.assertEqual(b.d, c.d)

    def test_length(self):
        a = Vector([0, 1, 2, 3])
        b = a.length()
        c = math.sqrt(14)

        self.assertEqual(b, c)

    def test_lenght(self):
        # Uncomment after passing
        self.assertAlmostEqual(Vector([2, 4]).length(), 4.47213595499, 3)
        self.assertAlmostEqual(Vector([2, 4, 5]).length(), 6.708203932499369, 3)
        return


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
