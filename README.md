[![Build Status](https://travis-ci.org/jurf/open-source-development-course-hw02-1.svg?branch=pr%2Fstep1)](https://travis-ci.org/jurf/open-source-development-course-hw02-1)

# Simple Vector implementation in python

Very simple vector implementation supporting basic operations.

## Usage

```python
from ossdev import Vector, Matrix
a = Vector([0, 1, 2, 3])
print(a)

m = Matrix.ident(4)
print(m)
print(m + m)
```

Operations:
- Addition/subtraction with a scalar `a + 1`
- Vector addition/subtraction: `a + b`
- Multiplication:
  - scalar * vector
  - row-vector * col-vector
  - col-vector * row-vector
- Bit-wise XOR: `k ^ a`
- Vector magnitude: `a.length()`
- `reverse()`, `hash()`, `repr()`, `reversed()`, `a[i] = k`

Matrix operations:
- Addition

## Installation

```bash
pip install -U --no-cache .
```
