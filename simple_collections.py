from typing import List

list_int = [1, 2, 3]
list_float = [1., 2., 3.]


def p_list(ll: List):
    print(len(ll))


def p_list_int(ll: List[int]):
    print(len(ll))

def p_list_float(ll: List[float]):
    print(len(ll))


p_list(list_int)
p_list(list_float)

p_list_int(list_int)
p_list_int(list_float)  # error: Argument 1 to "p_list_int" has incompatible type "List[float]"; expected "List[int]"

p_list_float(list_int)  # error: Argument 1 to "p_list_float" has incompatible type "List[int]"; expected "List[float]"
                        # note: "List" is invariant -- see http://mypy.readthedocs.io/en/latest/common_issues.html#variance
                        # note: Consider using "Sequence" instead, which is covariant

p_list_float(list_float)
