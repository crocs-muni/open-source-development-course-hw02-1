# Simple Vector implementation in python 

[![Python package](https://github.com/xsebek/open-source-development-course-hw02-1/actions/workflows/test.yaml/badge.svg)](https://github.com/xsebek/open-source-development-course-hw02-1/actions/workflows/test.yaml)

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
- Vector reverse `reversed(a)`
- Vector length `a.length()` (if you want dimension, use `len(a)`)
- ...many more!

## Installation

```bash
pip install -U --no-cache . 
```
