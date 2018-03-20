"""
Mypy will infer the first assignment as the variable's type
"""
from typing import List


class MusicBand:
    def __str__(self) -> str:
        return self.name

    def __init__(self, name) -> None:
        self.name = name


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


groups = [MusicBand("65daysofstatic"), MusicBand("Russian Circles"), MusicBand("Michel Louvain")]
cars = [CarModel("Honda", "Civic", 2015), CarModel("Toyota", "Matrix", 2007)]

my_eclectic_function(groups, cars)

my_eclectic_function([123], [456])  # error: List item 0 has incompatible type "int"; expected "MusicBand"
                                    # error: List item 0 has incompatible type "int"; expected "CarModel"
