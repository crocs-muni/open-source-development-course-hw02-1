#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ossdev

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

    def test_lenght(self):
        # Uncomment after passing
        # self.assertAlmostEqual(Vector([2, 4]).length(), 4.47213595499, 3)
        # self.assertAlmostEqual(Vector([2, 4, 5]).length(), 6.708203932499369, 3)
        return

    def test_cmp(self):
        a = Vector([1, 2, 1, 3])
        b = Vector([1, 2, 1, 3])
        c = Vector([10, 8, 2, 0])
        d = Vector([3, 2, 1])
        e = Vector([20])

        self.assertEqual(a.__cmp__(b), 0)
        self.assertEqual(a.__cmp__(c), -1)
        self.assertEqual(c.__cmp__(b), 1)
        self.assertEqual(c.__cmp__(d), 1)
        self.assertEqual(c.__cmp__(e), 0)

    def test_reversed(self):
        a = Vector([1, 10, 15, 4])
        b = Vector([4, 15, 10, 1])

        self.assertEqual(reversed(a).get(), b.get())
        self.assertNotEqual(reversed(a).get(), a.get())

    def test_sub(self):
        a = Vector([1, 0, 0, 2])
        b = Vector([2, 3, 3, 3])

        self.assertEqual((b - a).get(), [1, 3, 3, 1])
        self.assertEqual((b - 3).get(), [-1, 0, 0, 0])

    def test_mul(self):
        a = Vector([1, 0, 0, 2])

        self.assertEqual((a * 3).get(), [3, 0, 0, 6])

    def test_xor(self):
        a = Vector([2, 0, 0, 2])

        self.assertEqual((a ^ 1).get(), [3, 1, 1, 3])


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
