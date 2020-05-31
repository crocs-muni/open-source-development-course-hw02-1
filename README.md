[![Build Status](https://travis-ci.org/valcikeric/open-source-development-course-hw02-1.svg?branch=pr%2Fstep1)](https://travis-ci.org/valcikeric/open-source-development-course-hw02-1)
# Simple Vector implementation in python 

Very simple vector implementation supporting basic operations.

## Usage

```python
from ossdev import Vector
a = Vector([0, 1, 2, 3])
print(a)
```

Operations:
- Addition with a scalar `a+1`
- Vector addition: `a + b`
- Vector substraction: `a - b`
- Multiplication by a scalar: `a * 2`
- Invert vector: `-a`
- Reverse vector: `reversed(a)`
- Vector XOR: `a ^ 3`
- Vector length: `a.length()`
- Vector length comparison: 
```python
a == b
a != b
a < b
a <= b
a > b
b >= a
```

## Installation

```bash
pip install -U --no-cache . 
```
