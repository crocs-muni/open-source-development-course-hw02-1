# Simple Vector implementation in python 

Very simple vector implementation supporting basic operations.

## Usage

```python
from ossdev import Vector
a = Vector([0, 1, 2, 3])
print(a)
```

Operations:
- Set element: `a[1] = 1`
- Access to element: `a[1]`
- Get length: `a.length()`
- Comparison: `a < b`, `a > b`, `a == b`
- Negation: `-a`
- Addition with a scalar: `a+1`
- Vector addition: `a + b`
- Subtraction with a scalar: `a-1`
- Vector subtraction: `a - b`
- Multiplication with a scalar: `a * 2`
- XOR operation with a scalar: `a ^ 2`

## Installation

```bash
pip install -U --no-cache . 
```
