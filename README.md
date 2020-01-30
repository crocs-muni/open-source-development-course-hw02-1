[![Build Status](https://travis-ci.org/danzatt/open-source-development-course-hw02-1.svg?branch=master)](https://travis-ci.org/danzatt/open-source-development-course-hw02-1)

# Simple Vector implementation in python 

Very simple vector implementation supporting basic operations.

## Usage

```python
from ossdev import Vector, Matrix
a = Vector([0, 1, 2, 3])
b = Vector(size=7)  # contains 7 zeros
print(a)

m = Matrix.ident(4)
print(m)
print(m + m)
```

Operations:
- Addition with a scalar `a+1`
- Multiplication with a scalar `a+1`
- xor with a scalar `a+1`
- Vector addition: `a + b`
- Vector subtraction: `a - b`
- Multiplication:
  - scalar * vector
  - row-vector * col-vector
  - col-vector * row-vector

Matrix operations:
- Addition

Other operations:
- Dimension of the vector: `len(a)`
- Vector length: `a.length()`
- Negation of all coordinates: `-a`
- Reverse coordinates: `reversed(a)`
- Comparison operators: `a > b`
  - ***they compare length of the vectors***

## Installation

```bash
pip install -U --no-cache . 
```
