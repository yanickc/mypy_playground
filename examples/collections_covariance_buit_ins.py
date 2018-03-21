"""
Collections type invariance.

By default, Mypy considers built-in collections to be invariant with respect to their element type.
That is, you cannot substitute a list of "something" with a list of "something-else" even you could
convert "something-else" into "something"
"""

from typing import List, Sequence

list_int = [1, 2, 3]
list_float = [1., 2., 3.]

# MyPy will use the most general element type for its inference:

list_mixed = [1, 2, 3.14159]  # Revealed type is 'builtins.list[builtins.float*]'
list_mixed2 = [1, "2", 3.14159]  # Revealed type is 'builtins.list[builtins.object*]'


# reveal_type(list_mixed)

def len_list(ll: List):
    print(len(ll))


def len_list_int(ll: List[int]):
    print(len(ll))


def len_list_float(ll: List[float]):
    print(len(ll))


def len_list_sequence_float(ll: Sequence[float]):
    print(len(ll))


len_list(list_int)
len_list(list_float)

len_list_int(list_int)
len_list_int(list_float)  # error: Argument 1 to "p_list_int" has incompatible type "List[float]"; expected "List[int]"

len_list_float(list_float)
len_list_float(list_int)  # error: Argument 1 to "p_list_float" has incompatible type "List[int]"; expected "List[float]"
                          # note: "List" is invariant -- see http://mypy.readthedocs.io/en/latest/common_issues.html#variance
                          # note: Consider using "Sequence" instead, which is covariant

len_list_sequence_float(list_int)  # OK with Sequence, which is 'covariant'
