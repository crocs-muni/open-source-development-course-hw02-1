[![Build Status](https://travis-ci.org/danzatt/open-source-development-course-hw02-1.svg?branch=master)](https://travis-ci.org/danzatt/open-source-development-course-hw02-1)

# Simple Vector implementation in python 

Very simple vector implementation supporting basic operations.

## Usage

```python
from ossdev import Vector
a = Vector([0, 1, 2, 3])
b = Vector(size=7)  # contains 7 zeros
print(a)
```

Operations with scalar:
- Addition `a+1`
- Addition `2*a`
- xor `a^1`

Operations with another vector:
- Addition: `a + b`
- Subtraction: `a - b`

Other operations:
- Dimension of the vector: `len(a)`
- Vector length: `a.length()`
- Negation of all coordinates: `-a`
- Reverse coordinates: `reversed(a)`
- Comparison operators: `a > b`
  - ***they compare dimension of the vectors***

## Installation

```bash
pip install -U --no-cache . 
```
