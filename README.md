![Build status](https://github.com/drehak/open-source-development-course-hw02-1/actions/workflows/python-package.yml/badge.svg)

# Simple Vector implementation in python 

Very simple vector implementation supporting basic operations.

## Usage

```python
from ossdev import Vector
a = Vector([0, 1, 2, 3])
print(a)
```

Operations:
- Field access: `a[1]`
- Addition with a scalar: `a + 1`
- Multiplication with a scalar: `a * 3`
- XOR with a scalar: `a ^ 3`
- Vector subtraction: `a - b`
- Vector addition: `a + b`
- Vector comparison: `a < b`
- Vector negation: `-a`
- Vector length: `length(a)`
- Vector reversal: `reversed(a)`

## Installation

```bash
pip install -U --no-cache . 
```
