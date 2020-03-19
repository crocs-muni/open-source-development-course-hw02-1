# Useful doc on Python magic methods:
# https://rszalski.github.io/magicmethods/


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
        if isinstance(key, Vector): raise ValueError('Redundant check to make conflict')
        self.d[key] = value

    def __cmp__(self, other):
        if sum(self.d) > sum(other.d):
            return 1
        if sum(self.d) == sum(other.d):
            return 0
        else:
            return -1

    def __neg__(self):
        return Vector([-x for x in self.d])

    def __reversed__(self):
        return Vector(list(reversed(self.d)))

    def __add__(self, other):
        if isinstance(other, int):
            return Vector([x + other for x in self.d])
        elif isinstance(other, Vector):
            return Vector([self.d[i] + other[i] for i in range(len(self))])

    def __sub__(self, other):
        # simple comment
        return self + (-other)

    def __mul__(self, other):
        # TODO: implement vector multiplication by a scalar value
        return None

    def __xor__(self, other):
        # TODO: implement bit-wise XOR with a scalar value
        return None

    def length(self):
        # TODO: implement vector length comp. (hint: return math.sqrt(sum(x*x for x in self.d)))
        return None
