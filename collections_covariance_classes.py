"""
Collections type invariance. Built-in collections follow the
usual class hierarchy (Liskov) substitution principles.
"""
from typing import List


class MusicBand:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name


class Orchestra(MusicBand):
    def __init__(self, name) -> None:
        super().__init__(name)


class CarModel:
    def __str__(self) -> str:
        return f"{self.maker}, {self.name}, {self.year}"

    def __init__(self, maker, name, year) -> None:
        self.maker = maker
        self.name = name
        self.year = year


def my_eclectic_function(groups: List[MusicBand], cars: List[CarModel]):
    for g in groups:
        print(g, end=" ")
    print()
    for c in cars:
        print(c, end=" ")


groups = [MusicBand("65daysofstatic"), MusicBand("Russian Circles"), Orchestra("OM")]
cars = [CarModel("Honda", "Civic", 2015), CarModel("Toyota", "Matrix", 2007)]

my_eclectic_function(groups, cars)

my_eclectic_function([123], [456])  # error: List item 0 has incompatible type "int"; expected "MusicBand"
                                    # error: List item 0 has incompatible type "int"; expected "CarModel"
