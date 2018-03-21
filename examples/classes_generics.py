"""
Why make it simple?...

Python, being dynamically typed, has many generic constructs. See collections_covariance_buit_ins.py
For "generic" classes, we now need a way to describe generics.

(╯°□°）╯︵ ┻━┻


From http://mypy.readthedocs.io/en/stable/generics.html:

    The built-in collection classes are generic classes. Generic types have one or more type parameters, which can be
    arbitrary types. For example, Dict[int, str] has the type parameters int and str, and List[int] has a type parameter
    int.

    Programs can also define new generic classes. Here is a very simple generic class that represents a stack:
"""

from typing import TypeVar, Generic, List

T = TypeVar('T')


class Stack(Generic[T]):
    def pop(self) -> T:
        return self.items.pop()

    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def empty(self) -> bool:
        return not self.items


# Construct an empty Stack[int] instance
stack = Stack[int]()
stack.push(2)
stack.pop()
stack.push('x')  # error: Argument 1 to "push" of "Stack" has incompatible type "str"; expected "int"

# All or nothing affair, once we create a generic type,
# we need to "instanciate" its type to make it "concrete"
stack2 = Stack()  # error: Need type annotation for 'stack2'
