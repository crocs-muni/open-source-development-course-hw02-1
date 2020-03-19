[![Build Status](https://travis-ci.com/TomasJani/open-source-development-course-hw02-1.svg?branch=pr%2Fstep1)](https://travis-ci.com/TomasJani/open-source-development-course-hw02-1)

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
- Addition with a scalar `a+1`
- Vector addition: `a + b`
- Vector subtraction: `a - b`
- Vector reversed: `reversed(a)`
- Vector compere: `a < b (>, >=, <=, ==, ...)`
- Multiplication:
  - scalar * vector
  - row-vector * col-vector
  - col-vector * row-vector

Matrix operations:
- Addition

## Installation

```bash
pip install -U --no-cache . 
```
