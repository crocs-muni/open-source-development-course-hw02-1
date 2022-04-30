#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ossdev

import math
import unittest
from ossdev import Vector


class VectorTest(unittest.TestCase):
    """Simple vector tests"""

    def __init__(self, *args, **kwargs):
        super(VectorTest, self).__init__(*args, **kwargs)

    def test_math(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        c = a + b
        d = a - b
        e = a * 3
        f = a ^ 2

        self.assertEqual(c.get(), [3, 3, 3, 3])
        self.assertEqual(d.get(), [-3, -1, 1, 3])
        self.assertEqual(e.get(), [0, 3, 6, 9])
        self.assertEqual(f.get(), [2, 3, 0, 1])

        self.assertEqual(a.length(), math.sqrt(14))

    def test_setitem(self):
        v = Vector([0, 1, 2, 3])
        v[1] = 'a'

        self.assertEqual(v.get(), [0, 'a', 2, 3])

    def test_reversed(self):
        v = Vector([0, 1, 2, 3])

        self.assertEqual(reversed(v), [3, 2, 1, 0])

    def test_cmp(self):
        u = Vector([0, 1, 2, 3])
        v = Vector([0, 1, 2, 4])

        self.assertGreater(v, u)
        self.assertLess(u, v)
        self.assertNotEqual(u, v)
        self.assertEqual(u, u)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
