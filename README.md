[![Build Status](https://api.travis-ci.org/nitrajka/open-source-development-course-hw02-1.svg?branch=master)](https://travis-ci.org/nitrajka/open-source-development-course-hw02-1/)

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
- Addition with a scalar `a + 1`
- Vector addition: `a + b`
- Multiplication:
  - scalar * vector
  - row-vector * col-vector
  - col-vector * row-vector
- Setting a particular item in vector: `v[k] = n`
- Comparing vectors: `Vector([1]) < Vector([1, 2])` (+ other operations like: >, ==,  !=)
- Multiplication by scalar: `v1 * c`
- Vector bitwise XOR: `v1 ^ v2`
- Vector subtraction: `v1 - v2`
- Reversing a vector's content: `reversed(v)`
- Vector length: `len(v)`

Matrix operations:
- Addition

## Installation

```bash
pip install -U --no-cache . 
```
