#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ossdev

import unittest
from ossdev import Vector

import math


class VectorTest(unittest.TestCase):
    """Simple vector tests"""

    def __init__(self, *args, **kwargs):
        super(VectorTest, self).__init__(*args, **kwargs)

    def test_cmp(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        self.assertEquals(a.__cmp__(b), -1)

    def test_reversed(self):
        a = reversed(Vector([1, 2, 3, 4, 5, 6, 7]))
        self.assertEqual(a.get(), [7, 6, 5, 4, 3, 2, 1])

    def test_add(self):
        a = Vector([0, 1, 2, 3])
        b = 5
        c = Vector([3, 2, 1, 0])
        x = Vector([1, 2])

        self.assertEqual((a + b).get(), [5, 6, 7, 8])
        self.assertEqual((a + c).get(), [3, 3, 3, 3])
        self.assertRaises(ValueError, lambda: a + x)
        self.assertRaises(ValueError, lambda: a + "foo")

    def test_setitem(self):
        a = Vector([1, 1, 1, 1, 1])
        a[2] = 0
        self.assertEqual(a.get(), [1, 1, 0, 1, 1])

    def test_sub(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([-3, -2, -1, -0])
        c = a - b

        self.assertEqual(c.get(), [3, 3, 3, 3])

    def test_mul(self):
        a = Vector([1, 2, 3, 4])
        b = 7
        c = Vector([7, 7, 7, 7])
        x = Vector([1, 2])

        self.assertEqual((a * b).get(), [7, 14, 21, 28])
        self.assertEqual((a * c).get(), [7, 14, 21, 28])
        self.assertRaises(ValueError, lambda: a * x)
        self.assertRaises(ValueError, lambda: a * "foo")

        s = Vector([1, 2]).transpose()
        t = Vector([2, -1])
        self.assertEqual(s * t, 0)

    def test_xor(self):
        a = Vector([1, 2, 3])
        b = 2
        c = Vector([2, 2, 2])
        x = Vector([1, 2])

        self.assertEqual((a ^ b).get(), [3, 0, 1])
        self.assertEqual((a ^ c).get(), [3, 0, 1])
        self.assertRaises(ValueError, lambda: a ^ x)
        self.assertRaises(ValueError, lambda: a ^ "foo")

    def test_and(self):
        a = Vector([1, 2, 3])
        b = 2
        c = Vector([2, 2, 2])
        x = Vector([1, 2])

        self.assertEqual((a & b).get(), [0, 2, 2])
        self.assertEqual((a & c).get(), [0, 2, 2])
        self.assertRaises(ValueError, lambda: a & x)
        self.assertRaises(ValueError, lambda: a & "foo")

    def test_length(self):
        a = Vector([3, 4])
        self.assertEqual(a.length(), 5)

        b = Vector([1, 2, 3, 4, 5])
        self.assertAlmostEqual(b.length(), math.sqrt(55))

        c = Vector([])
        self.assertAlmostEqual(c.length(), 0)

    def test_dot(self):
        a = Vector([1, 2])
        b = Vector([2, -1])
        self.assertEqual(a.dot(b), 0)

        x = Vector([1])
        self.assertRaises(ValueError, lambda: a.dot(x))

    def test_transpose(self):
        a = Vector([1, 2])
        self.assertEqual(a.is_row, False)
        a = a.transpose()
        self.assertEqual(a.is_row, True)
        a = a.transpose()
        self.assertEqual(a.is_row, False)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
