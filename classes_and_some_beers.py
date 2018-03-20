"""
No surprise here, straightforward class inheritance is checked.
And good beer...
"""


class Beer:
    pass


class TopFermenting(Beer):
    pass


class AleType(TopFermenting):
    pass


class WheatBeer(TopFermenting):
    pass


class CreamAle(AleType):
    pass


class AmericanAle(AleType):
    pass


class Bitter(AmericanAle):
    pass


class BestBitter(Bitter):
    pass


class PaleAle(BestBitter):
    pass


class IndiaPaleAle(PaleAle):
    pass


def drink(b: Beer):
    print(b)


def enjoy(b: Bitter):
    print(b)


some_beer = CreamAle()
good_beer = IndiaPaleAle()

drink(some_beer)
enjoy(some_beer)  # error: Argument 1 to "enjoy" has incompatible type "CreamAle"; expected "Bitter"
enjoy(good_beer)

# Reassignment
#
# Each name within a function only has a single ‘declared’ type.
# This is related to invariance. See READM.md

good_beer = WheatBeer()  # error: Incompatible types in assignment (expression has type "WheatBeer", variable has type "IndiaPaleAle")

# We can make explicit that a variable has a base type

tasters_beer: AleType = IndiaPaleAle()
tasters_beer = AmericanAle()  # No problem here.
