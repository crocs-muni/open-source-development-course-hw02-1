#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ossdev

import unittest
from ossdev import Vector


class VectorTest(unittest.TestCase):
    """Simple vector tests"""

    def __init__(self, *args, **kwargs):
        super(VectorTest, self).__init__(*args, **kwargs)

    def test_set(self):
        a = Vector([0, 0, 0])
        a[1] = 4
        a[2] = 8

        self.assertEqual(a.get(), [0, 4, 8])

    def test_cmp_less(self):
        self.assertTrue((Vector([1, 2, 3]) < Vector([1, 3, 3])))

    def test_cmp_more(self):
        self.assertTrue((Vector([1, 2, 3]) > Vector([1, 1, 3])))

    def test_cmp_equal(self):
        self.assertTrue((Vector([1, 2, 3]) == Vector([1, 2, 3])))

    def test_reversed(self):
        self.assertEqual(reversed(Vector([1, 2, 3])), Vector([3, 2, 1]))

    def test_add(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        c = a + b

        self.assertEqual(c.get(), [3, 3, 3, 3])

    def test_sub(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        c = a - b

        self.assertEqual(c.get(), [-3, -1, 1, 3])

    def test_mul(self):
        a = Vector([0, 1, 2, 3])
        b = a * 2

        self.assertEqual(b.get(), [0, 2, 4, 6])

    def test_xor(self):
        a = Vector([0, 1, 5, 3])
        b = a ^ 3

        self.assertEqual(b.get(), [3, 2, 6, 0])

    def test_length(self):
        self.assertEqual(len(Vector(size=10)), 10)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
