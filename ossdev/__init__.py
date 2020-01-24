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
        self.d[key] = value
        return self.d[key]

    def __cmp__(self, other):
        # TODO: implement, -1 if self < other, 0 if self == other, 1 if self > other
        s = 0
        o = 0
        for i in self.d:
            s += i**2
        for j in other.d:
            o += j**2
        s = math.sqrt(s)
        o = math.sqrt(o)

        if s < o:
            ret = -1
        elif s == o:
            ret = 0
        else:
            ret = 1
        return ret

    def __neg__(self):
        return Vector([-x for x in self.d])

    def __reversed__(self):
        # TODO: implement vector element reversal (hint: list(reversed(self.d)))
        return list(reversed(self.d))

    def __add__(self, other):
        if isinstance(other, int):
            return Vector([x + other for x in self.d])
        elif isinstance(other, Vector):
            return Vector([self.d[i] + other[i] for i in range(len(self))])

    def __sub__(self, other):
        # TODO: implement vector subtraction
        return [s - o for s, o in zip(self, other)]

    def __mul__(self, other):
        # TODO: implement vector multiplication by a scalar value
        return [s * other for s in self.d]

    def __xor__(self, other):
        # TODO: implement bit-wise XOR with a scalar value
        ret = []
        for s in self.d:
            ret.append(s ^ other)
        return ret

    def length(self):
        # TODO: implement vector length comp. (hint: return math.sqrt(sum(x*x for x in self.d)))
        return math.sqrt(sum(x*x for x in self.d))
