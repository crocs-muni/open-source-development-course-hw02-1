[![Build Status](https://api.travis-ci.org/nitrajka/open-source-development-course-hw02-1.svg?branch=master)](https://travis-ci.org/nitrajka/open-source-development-course-hw02-1/)

# Simple Vector implementation in python 

Very simple vector implementation supporting basic operations.

## Usage

```python
from ossdev import Vector
a = Vector([0, 1, 2, 3])
print(a)
```

Operations:
- Addition with a scalar `a + 1`
- Vector addition: `a + b`
- Setting a particular item in vector: `v[k] = n`
- Comparing vectors: `Vector([1]) < Vector([1, 2])` (+ other operations like: >, ==,  !=)
- Vector multiplication: `v1 * v2`
- Vector bitwise XOR: `v1 ^ v2`
- Vector subtraction: `v1 - v2`
- Reversing a vector's content: `reversed(v)`
- Vector length: `len(v`

## Installation

```bash
pip install -U --no-cache . 
```
