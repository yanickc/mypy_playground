"""
None is a silent citizen in Python.
Once we start typing stuff, we need to think about None.

None exists, but still... it's None... ¯\_(ツ)_/¯
"""


class Citation:
    def __init__(self, text) -> None:
        self.text = text


def get_citation(should: bool) -> Citation:
    if should:
        return Citation("Null References: The Billion Dollar Mistake")
    else:
        return None
        # STEP 1
        #
        # MyPy will detect this with the `--strict-optional` flag :
        #
        #   error: Incompatible return value type (got "None", expected "Citation")
        #
        # Fix with return type :
        #   -> Optional[Citation]


c = get_citation(True)

# STEP 2: error: Item "None" of "Optional[Citation]" has no attribute "text"
print(c.text)








# continued...







class Something():
    pass


def bring_it_on(i_should: bool) -> Something:  # Fix me
    return Something() if i_should else None
        # PyCharm does not highlight...
        #
        # ...but MyPy will detect this with the `--strict-optional` flag :
        #
        #   error: Incompatible return value type (got "Optional[Something]", expected "Something")
        # Fix with return type :
        #   -> Optional[Something]

b1 = bring_it_on(False)
if b1 is None:
    print("oh! no!")
