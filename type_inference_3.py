"""
Mypy will infer the first assignment as the variable's type
"""
from typing import Optional


class Something():
    pass


def bring_it_on(i_should: bool) -> Something:
    if i_should:
        return Something()
    else:
        return None
        # PyCharm highlights this
        #
        # MyPy will detect this with the `--strict-optional` flag :
        #       
        #   error: Incompatible return value type (got "None", expected "Something")
        # Fix with return type :
        #   -> Optional[Something]


def bring_it_again(i_should: bool) -> Something:
    return Something() if i_should else None
    # Note here PyCharm does not highlight, but
    #
    # MyPy will detect this with the `--strict-optional` flag :
    #
    #   error: Incompatible return value type (got "None", expected "Something")
    # Fix with return type :
    #   -> Optional[Something]


b1 = bring_it_on(False)
if b1 is None:
    print("oh! no!")
