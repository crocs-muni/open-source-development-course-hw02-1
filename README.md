[![Build Status](https://travis-ci.com/JayDee81/open-source-development-course-hw02-1.svg?branch=master)](https://travis-ci.com/JayDee81/open-source-development-course-hw02-1)
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
- Set vector item `v.__setitem__(1, 2)`
- Compare vectors `v1.__cmp__(v2)`
- Reverse vector `v.__reversed__()`
- Subtract vectors `v1.__sub__(v2)`
- Multiply vector by scalar `v.__mul__(5)`
- Bit-wise xor vector with scalar `v.__xor__(4)`
- Vector length `v.length()`

## Installation

```bash
pip install -U --no-cache . 
```
