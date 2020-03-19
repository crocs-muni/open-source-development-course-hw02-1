#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ossdev

import unittest
from ossdev import Vector
from math import sqrt

class VectorTest(unittest.TestCase):
    """Simple vector tests"""

    def __init__(self, *args, **kwargs):
        super(VectorTest, self).__init__(*args, **kwargs)

    def test_add(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        c = a + b

        self.assertEqual(c.get(), [3, 3, 3, 3])

    def test___setitem__(self):
        a = Vector([0, 0, 0, 0])
        a[1] = 1
        a[3] = 2
        self.assertEqual(a.get(), [0, 1, 0, 2])

    def test___lt__(self):
        a = Vector([0, 0, 0, 0])
        b = Vector([1, 1, 1, 1])
        self.assertTrue(a < b)

    def test___eq__(self):
        a = Vector([])
        b = Vector([])
        c = Vector([0, 0, 0, 0])
        d = Vector([0, 0, 0, 0])
        self.assertTrue(a == b)
        self.assertTrue(c == d)
        self.assertTrue(a == c)

    def test___reversed__(self):
        a = Vector([])
        b = Vector([1])
        c = Vector([0, 1, 2, 3])
        self.assertEqual(a.__reversed__().get(), [])
        self.assertEqual(b.__reversed__().get(), [1])
        self.assertEqual(c.__reversed__().get(), [3, 2, 1, 0])

    def test___sub__(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        c = b - a

        self.assertEqual(c.get(), [3, 1, -1, -3])

    def test___mul__(self):
        a = Vector([1, 1, 2, 2])
        b = Vector([2, 2, 1, 1])
        c = a * b

        d = Vector([])
        e = Vector([])
        f = d * e

        self.assertEqual(c.get(), [2, 2, 2, 2])
        self.assertEqual(f.get(), [])

    def test___xor__(self):
        a = Vector([1, 1, 2, 2])
        b = Vector([2, 2, 1, 1])
        c = a ^ b

        d = Vector([])
        e = Vector([])
        f = d ^ e

        self.assertEqual(c.get(), [3, 3, 3, 3])
        self.assertEqual(f.get(), [])

    def test_length(self):
        a = Vector([])
        b = Vector([3, 2, 2])

        self.assertEqual(a.length(), 0)
        self.assertEqual(b.length(), sqrt(17))


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
