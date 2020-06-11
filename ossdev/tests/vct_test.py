#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ossdev

import unittest
from ossdev import Vector, Matrix


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
    
    def test_eq(self):
        a = Vector([1, 2, 4])
        b = Vector([1, 2, 3])

        self.assertFalse(a == b)

    def test_reversed(self):
        a = Vector([1, 2, 3])
        rev = reversed(a)

        self.assertEqual(rev, Vector([3, 2, 1]))
    
    def test_sub(self):
        a = Vector([3, 3, 2])
        b = Vector([1, 1, 1])
        c = a - b

        self.assertEqual(c, Vector([2, 2, 1]))
    
    def test_mul_with_scalar(self):
        a = Vector([1, 2, 3]) * 2

        self.assertEqual(a, Vector([2, 4, 6]))

    def test_mul_with_vector(self):
        a = Vector([1, 2, 1]) * Vector([1, 2, 3])

        self.assertEqual(a, Vector([1, 4, 3]))

        b = Vector([1, 2, 3])
        b.row = True
        dot_product = b * Vector([2, 3, 4])

        self.assertEqual(dot_product, 20)
    
    def test_xor(self):
        a = Vector([7, 3])
        ret = a ^ 3

        self.assertEqual(ret, Vector([4, 0]))
    
    def test_and_scalar(self):
        a = Vector([1, 2, 3])

        self.assertEqual(a & 1, Vector([1, 0, 1]))

    def test_and_vector(self):
        a = Vector([1, 2, 3])
        b = Vector([2, 3, 4])

        self.assertEqual(a & b, Vector([0, 2, 0]))

    def test_lenght(self):
        self.assertAlmostEqual(Vector([2, 4]).length(), 4.47213595499, 3)
        self.assertAlmostEqual(Vector([2, 4, 5]).length(), 6.708203932499369, 3)
        return
    
    def test_transpose(self):
        a = Vector([1, 2, 3])
        b = a.transpose()

        self.assertTrue(b.row)
    
    def test_matrix_add(self):
        a = Matrix.square(2)
        b = Matrix.ident(2)

        a[0][0] = 4
        b[0][1] = 3

        ab = a + b

        self.assertEqual(ab[0][0], 5)
        self.assertEqual(ab[0][1], 3)
        self.assertEqual(ab[1][0], 0)
        self.assertEqual(ab[1][1], 1)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
