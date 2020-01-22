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

    def test_set(self):
        v1 = Vector([0, 1])
        v1[0] = 1
        self.assertEqual(v1.get(), [1, 1])

        with self.assertRaises(Exception) as c:
            v1.__setitem__(2, 2)

    def test_cmp(self):
        v1 = Vector([1])
        v2 = Vector([])

        self.assertEqual(1, v1.__cmp__(v2))

        v2 = Vector([1, 2])
        self.assertEqual(1, v2.__cmp__(v1))

        v1 = Vector([1, 2])
        self.assertEqual(0, v1.__cmp__(v2))

    def test_reversed(self):
        v1 = Vector([1, 2, 3, 4, 5])
        v2 = Vector([1])

        self.assertEqual([5, 4, 3, 2, 1], v1.__reversed__().get())
        self.assertEqual([1], v2.__reversed__().get())

    def test_subtract(self):
        v1 = Vector([1, 2, 3, 4])
        v2 = Vector([1, 1, 1, 1])

        self.assertEqual([0, 1, 2, 3], (v1 - v2).get())

    def test_multiply(self):
        v1 = Vector([0, 1, 2])
        self.assertEqual([0, 2, 4], (v1 * 2).get())

    def test_xor(self):
        v1 = Vector([0, 1, 2, 4])
        self.assertEqual([3, 2, 1, 7], (v1 ^ 3).get())

    def test_length(self):
        self.assertEqual(0, len(Vector([])))
        self.assertEqual(2, len(Vector([0, 1])))


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
