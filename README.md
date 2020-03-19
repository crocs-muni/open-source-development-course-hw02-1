[![Build Status](https://travis-ci.com/cucak559/open-source-development-course-hw02-1.svg?branch=pr%2Fstep1)](https://travis-ci.com/cucak559/open-source-development-course-hw02-1)

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
- Vector multiplication: `a * b`
- Vector xor: `a ^ b`
- Vector substraction: `a - b`
- Vector length: `a.length()`
- Vector comparing, eg: `a < b`

## Installation

```bash
pip install -U --no-cache . 
```
