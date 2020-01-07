# Useful doc on Python magic methods:
# https://rszalski.github.io/magicmethods/

import math


class Vector:
    def __init__(self, arr=None, size=None):
        self.d = arr if arr is not None else (([0] * size) if size else [])

    @classmethod
    def from_arr(cls, arr):
        return Vector(arr=arr)

    @classmethod
    def from_size(cls, size):
        return Vector(size=size)

    def set(self, arr):
        self.d = arr
        return self

    def get(self):
        return self.d

    def __len__(self):
        return len(self.d)

    def __repr__(self):
        return str(self.d)

    def __getitem__(self, item):
        return self.d[item]

    def __hash__(self):
        return sum(self.d)

    def __setitem__(self, key, value):
        # TODO: implement

        if key >= len(self.d):
            self.d += [0] * (key - len(self.d) + 1)

        self.d[key] = value

        return None

    def __cmp__(self, other):
        # TODO: implement, -1 if self < other, 0 if self == other, 1 if self > other
        eq = false not in [i == j for i, j in zip(self.d, other.get())]

        if eq:
            return 0
        else:
            return -1 if length() < other.length() else 1

    def __neg__(self):
        return Vector([-x for x in self.d])

    def __reversed__(self):
        # TODO: implement reversed (hint: list(reversed(self.d))))
        vec = Vector(list(reversed(self.d)))

        for x in vec.get():
            yield x

    def __add__(self, other):
        if isinstance(other, int):
            return Vector([x + other for x in self.d])
        elif isinstance(other, Vector):
            return Vector([self.d[i] + other[i] for i in range(len(self))])

    def __sub__(self, other):
        # TODO: implement vector subtraction
        # a simple comment
        return self + (-other)

    def __mul__(self, other):
        # TODO: implement vector multiplication by a scalar value

        if isinstance(other, int):
            return Vector([x * other for x in self.d])
        elif isinstance(other, Vector):
            return Vector([self.d[i] * other[i] for i in range(len(self))])

    def __xor__(self, other):
        # TODO: implement bit-wise XOR with a scalar value
        return Vector([x ^ other for x in self.d])

    def length(self):
        # TODO: implement vector length comp. (hint: return math.sqrt(sum(x*x for x in self.d)))
        return math.sqrt(sum(x*x for x in self.d))
