"""
Structural/Duck Typing vs Nominal Typing
Using pypi typing_extensions Protocol
"""
from typing_extensions import Protocol
from typing import List


class SupportsApply(Protocol):
    def apply(self, img: List[List[int]]) -> dict:
        pass


# notice Model doesn't need to inherit from SupportsApply
class MyClass:
    def apply(self, img: List[List[int]]) -> dict:
        return {}


class MyClassWithWrongApplySignature:
    def apply(self) -> None:
        return None


sa: SupportsApply = MyClass()

# note: Following member(s) of "MyClassWithWrongApplySignature" have conflicts:
# note:     Expected:
# note:         def apply(self, img: List[List[int]]) -> Dict[Any, Any]
# note:     Got:
# note:         def apply(self) -> None
sa2: SupportsApply = MyClassWithWrongApplySignature()
