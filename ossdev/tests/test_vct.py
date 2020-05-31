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
    
    def test_setitem(self):
        a = Vector([0, 0])
        a[1] = 4

        self.assertEqual(a.d, [0, 4])
    
    def test_eq(self):
        a = Vector([1, 2, 3])
        b = Vector([1, -2, 3])

        self.assertEqual(a == b, True)

    def test_cmp(self):
        a = Vector([1, 1])
        b = Vector([1, 3])

        self.assertEqual(a > b, False)
        self.assertEqual(b > a, True)

    def test_reversed(self):
        a = Vector([1, 2, 3])
        rev = reversed(a)

        self.assertEqual(rev, Vector([3, 2, 1]))
    
    def test_sub(self):
        a = Vector([3, 3, 2])
        b = Vector([1, 1, 1])
        c = a - b

        self.assertEqual(c, Vector([2, 2, 1]))
    
    def test_mul(self):
        a = Vector([1, 2, 3]) * 2

        self.assertEqual(a, Vector([2, 4, 6]))
    
    def test_xor(self):
        a = Vector([7, 3])
        ret = a ^ 3

        self.assertEqual(ret, Vector([4, 0]))

    def test_length(self):
        a = Vector([3, 4])

        self.assertEqual(a.length(), 5)

if __name__ == "__main__":
    unittest.main()  # pragma: no cover
