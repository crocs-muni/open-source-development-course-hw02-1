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
        self.assertEqual(Vector([1, 1, 1]), Vector([1, 1, 1]))
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
        self.assertFalse(res == None)
        self.assertEqual(res.get(), [1 ^ 3, 2 ^ 3, 3 ^ 3])

    def test_vector_xor(self):
        a = Vector([1, 1, 1])
        b = Vector([4, 5, 6])
        self.assertEqual(b ^ 1, b ^ a)

    def test_vector_and(self):
        a = Vector([1, 0, 1, 0])
        b = Vector([0, 1, 0, 1])
        res = a & b
        self.assertFalse(any(res.get()))

        a = Vector([1, 1, 1, 1])
        b = Vector([1, 1, 1, 1])
        res = a & b
        self.assertTrue(all(res.get()))

    def test_length(self):
        self.assertEqual(Vector([1, 0, 0]).length(), 1)
        self.assertEqual(Vector([2, 2, 2, 2]).length(), 4)

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
        self.assertAlmostEqual(Vector([2, 4]).length(), 4.47213595499, 3)
        self.assertAlmostEqual(Vector([2, 4, 5]).length(), 6.708203932499369, 3)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
