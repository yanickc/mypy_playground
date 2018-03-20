# Iterators

import itertools
from typing import Iterator


# Interesting convoluted example of a generator.
# NOT a good way to factorize primes ;-)

def iter_primes() -> Iterator[int]:
    numbers = itertools.count(2)  # An iterator of all numbers between 2 and +infinity

    # Generate primes forever
    while True:
        # Get the first number from the iterator (always a prime)
        prime = next(numbers)
        yield prime

        # This code iteratively builds up a chain of filters...
        numbers = filter(lambda x: x % prime, numbers)


for p in iter_primes():
    if p > 20:
        break
    print(p, end=" ")
