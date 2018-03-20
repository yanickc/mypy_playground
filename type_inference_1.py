"""
Mypy will infer the first assignment as the variable's type
"""


def name() -> str:
    return "Toupie"


s = name()  # Mypy decides here that `s` is a str
print(s)

s = 123  # error: Incompatible types in assignment (expression has type "int", variable has type "str")

n = 123
n = name()  # error: Incompatible types in assignment (expression has type "str", variable has type "int")
print(n)

# -----------------

# This may look strange, but is due to type invariance. See README.md -- About covariance section.

arr = []
arr = [1, 2, 3]  # error: Need type annotation for 'arr'
