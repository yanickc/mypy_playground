"""
Mypy will infer the first assignment as the variable's type
"""
from typing import List


def name() -> str:
    return "Toupie"


s = name()  # Mypy decides here that `s` is a str
print(s)

s = 123  # error: Incompatible types in assignment (expression has type "int", variable has type "str")

n = 123
n = name()  # error: Incompatible types in assignment (expression has type "str", variable has type "int")
print(n)

# -----------------------------------------------------------------------------

# This may look strange, but is due to type invariance.
# See README.md -- About covariance section.
# See also `collections_covariance_buit_ins.py`

arr = []  # error: Need type annotation for 'arr'
arr = [1, 2, 3]

arr2: List = []
arr2 = [1, 2, 3]

