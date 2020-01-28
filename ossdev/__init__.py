# Useful doc on Python magic methods:
# https://rszalski.github.io/magicmethods/
import itertools
import math


class Vector:
    def __init__(self, arr=None, size=None):
        self.d = list(arr) if arr is not None else (([0] * size) if size else [])
        self.row = False

    @classmethod
    def from_arr(cls, arr):
        return Vector(arr=list(arr))

    @classmethod
    def from_size(cls, size):
        return Vector(size=size)

    def set(self, arr):
        self.d = arr
        return self

    def get(self):
        return self.d

    def clone(self):
        return Vector.from_arr(list(self.get()))

    @property
    def is_row(self):
        return self.row

    def __len__(self):
        return len(self.d)

    def __repr__(self):
        return str(self.d)

    def __str__(self):
        return 'Vct%s' % self.d

    def __getitem__(self, item):
        return self.d[item]

    def __hash__(self):
        return sum(self.d)

    def __setitem__(self, key, value):
        if isinstance(key, Vector): raise ValueError('Redundant check to make conflict')
        self.d[key] = value

    def __cmp__(self, other):
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
        return list(reversed(self.d))

    def __add__(self, other):
        if isinstance(other, int):
            return Vector([x + other for x in self.d])
        elif isinstance(other, Vector):
            if len(self) != len(other): raise ValueError('Incompatible size')
            return Vector([self.d[i] + other[i] for i in range(len(self))])

    def __sub__(self, other):
        # you may use __add__() and negation, like return (-self + other)
        return [s - o for s, o in zip(self, other)]

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector([s * other for s in self.d])
        elif isinstance(other, Vector):
            if self.d.__len__() != other.d.__len__():
                raise ValueError('Different size vectors')
            if self.is_row == other.is_row:
                return Vector([self.d[i] * other[i] for i in range(len(self))])  # Hadamard product
            elif self.is_row:
                return self.dot(other)  # row x col is a dot-product (check matrix mult.)
            else:
                m = Matrix.square(len(self))  # a matrix
                for i, j in m.index_iter():
                    m[i][j] = self[i] * other[j]
                return m
        else:
            raise ValueError('Invalid operand')

    def __xor__(self, other):
        if isinstance(other, int):
            return Vector([self.d[i] ^ other for i in range(len(self))])
        elif isinstance(other, Vector):
            if self.d.__len__() != other.d.__len__():
                raise ValueError('Different size vectors')
            else:
                return Vector([self.d[i] ^ other[i] for i in range(len(self))])
        else:
            raise ValueError('Invalid operand')

    def __and__(self, other):
        if isinstance(other, int):
            return Vector([x & other for x in self.d])
        elif isinstance(other, Vector):
            if self.d.__len__() != other.d.__len__():
                raise ValueError('Different size vectors')
            return Vector([self.d[i] & other[i] for i in range(len(self))])
        else:
            raise ValueError('Invalid operand')

    def length(self):
        if len(self) == 0:
            return 0
        return math.sqrt(sum(x * x for x in self.d))

    def dot(self, other):
        return sum(self[i]*other[i] for i in range(len(self)))

    def transpose(self):
        v = Vector(self.d)
        v.row = not self.row
        return v


class Matrix:
    def __init__(self, dim):
        self._dim = dim
        self.vs = [Vector.from_size(dim[1]) for _ in range(dim[0])]

    @property
    def dim(self):
        return self._dim

    @property
    def rows(self):
        return self.dim[0]

    @property
    def cols(self):
        return self.dim[1]

    def index_iter(self):
        return itertools.product(range(self.rows), range(self.cols))

    def __getitem__(self, item):
        return self.vs[item]

    def __setitem__(self, key, value):
        self.vs[key] = Vector.from_arr(value.get())

    def __repr__(self):
        return ', '.join([repr(x) for x in self.vs])

    def __str__(self):
        return 'Matrix: [\n ' + '\n '.join([repr(x) for x in self.vs]) + '\n]'

    @classmethod
    def from_matrix(cls, o):
        m = Matrix(o.dim)
        for i, j in m.index_iter():
            m[i][j] = o[i][j]
        return m

    @classmethod
    def square(cls, n):
        return cls((n, n))

    @classmethod
    def ident(cls, n):
        m = cls.square(n)
        for i in range(n):
            m[i][i] = 1
        return m

    def check_matrix(self, other):
        if not isinstance(other, Matrix):
            raise ValueError('Not a matrix')

    def check_dim(self, other):
        self.check_matrix(other)
        if self._dim != other.dim:
            raise ValueError('Incompatible matrix')

    def __add__(self, other):
        self.check_dim(other)
        m = Matrix.from_matrix(self)
        for i, j in self.index_iter():
            m[i][j] = m[i][j] + other[i][j]
        return m
