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


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
