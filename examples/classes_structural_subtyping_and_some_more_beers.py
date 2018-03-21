"""
Class D is a structural subtype of class C if the former has all attributes
and methods of the latter, and with compatible types.

MyPy uses many `protocols` from typing:
    Iterable[T]  for  def __iter__(self) -> Iterator[T]

    Iterator[T]  for  def __next__(self) -> T
                      def __iter__(self) -> Iterator[T]

    Sized        for  def __len__(self) -> int

    Container[T] for  def __contains__(self, x: object) -> bool

    etc...

    See https://docs.python.org/3/library/typing.html

    But wait... What are those [T] ??? See classes_generics.py
     
"""

from typing import Iterator, Iterable, Sized


class BeerCrate:

    def __init__(self, nb_bottles) -> None:
        self.nb_bottles = nb_bottles

    def __iter__(self) -> Iterator[str]:
        count = self.nb_bottles
        while count > 1:
            yield f"{count} bottles of beer on the wall, {count} bottles of beer,\nTake one down and pass it around, {count-1} bottles of beer on the wall.\n"
            count -= 1
        yield f"1 bottle of beer on the wall, 1 bottles of beer,\nTake one down and pass it around, no more bottle of beer on the wall.\n"
        yield f"No more bottle of beer on the wall, no more bottle of beer.\nGo to the store and buy some more, {self.nb_bottles} bottles of beer on the wall.bottle of beer on the wall, 1 bottles of beer\nTake one down and pass it around, no more bottle of beer on the wall.\n"

    def __len__(self) -> int:
        return self.nb_bottles


def print_song(items: Iterable[str]):
    for x in items:
        print(x)


def print_time_to_sing(items: Sized):
    print(f"\n{len(items)} minutes to drink that song:\n")


beers = BeerCrate(5)
print_time_to_sing(beers)
print_song(beers)

my_song = ['a', 'b', 'c']
print_time_to_sing(my_song)
print_song(my_song)

