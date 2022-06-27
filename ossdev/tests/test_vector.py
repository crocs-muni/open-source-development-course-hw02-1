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

    def test_len(self):
        a = Vector([0, 1])
        self.assertEqual(len(a), 2)
        self.assertEqual(a.length(), 1.0)

    def test_reversed(self):
        a = Vector([0, 1, 2])
        self.assertEqual(reversed(a).get(), [2,1,0])
    
    def test_set(self):
        a = Vector([0, 1, 2])
        a[1] = 42
        self.assertEqual(a.get(), [0,42,2])

if __name__ == "__main__":
    unittest.main()  # pragma: no cover
