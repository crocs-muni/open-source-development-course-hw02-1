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
        for i in range(3):
            a[i] = 1

        for i in range(3):
            self.assertEqual(a[i], 1)

    def test_cmp(self):
        #self.assertEqual(Vector([1, 1, 1]), Vector([1, 1, 1]))
        self.assertGreater(Vector([1, 1]), Vector([1]))

    def test_neg(self):
        a = Vector([1, 1, 1])
        b = Vector([1, -1, 1])
        self.assertEqual((-a).get(), [-1, -1, -1])
        self.assertEqual((-b).get(), [-1, 1, -1])

    def test_reversed(self):
        self.assertEqual(reversed(Vector([1, 2, 3])).get(), [3, 2, 1])

    def test_sub(self):
        res = Vector([1, 2, 3]) - Vector([1, 2, 3])
        self.assertEqual(res.get(), [0, 0, 0])

        res = Vector([2, 2, 2]) - Vector([1, 1, 1])
        self.assertEqual(res.get(), [1, 1, 1])

    def test_mul(self):
        res = Vector([1, 2, 3]) * 2
        self.assertEqual(res.get(), [2, 4, 6])

    def test_xor(self):
        res = Vector([1, 2, 3]) ^ 3
        self.assertEqual(res.get(), [1 ^ 3, 2 ^ 3, 3 ^ 3])

    def test_length(self):
        self.assertEqual(Vector([1, 0, 0]).length(), 1)
        self.assertEqual(Vector([2, 2, 2, 2]).length(), 4)

    def test_add(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        c = a + b

        self.assertEqual(c.get(), [3, 3, 3, 3])


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
