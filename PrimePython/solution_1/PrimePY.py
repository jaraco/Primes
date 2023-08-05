"""
Python Prime Sieve
"""

import math


class Sieve:
    primes: list[bool]
    """Storage for sieve - since we filter evens, just half as many bits"""

    limit: int
    """Upper limit, highest prime we'll consider"""

    known = {
        10: 4,
        100: 25,
        1000: 168,
        10000: 1229,
        100000: 9592,
        1000000: 78498,
        10000000: 664579,
        100000000: 5761455,
    }
    """
    Historical data for validating results - the number of primes
    to be found under some limit, such as 168 primes under 1000.
    """

    def __init__(self, limit=1000000):
        self.limit = limit
        self.primes = [True] * (int((self.limit + 1) / 2))

    def get(self, index):
        """
        Get a bit from the array of bits, but automatically just filter out
        even numbers as false,
        and then only use half as many bits for actual storage
        """
        # even numbers are automaticallty returned as non-prime
        return self.primes[index // 2] if index % 2 else False

    def factors(self):
        factor = 3
        q = math.sqrt(self.limit)
        while factor < q:
            factor = next(filter(self.get, range(factor, self.limit)))
            yield factor
            factor += 2

    def clear_all(self):
        for factor in self.factors():
            self.clear(factor)

    def clear(self, factor):
        """
        Mark all multiples of factor as not prime.
        """
        # Start with the 3rd factor (2nd factor is a multiple of 2).
        self.primes[factor * 3 // 2 :: factor] = [False] * (
            (self.limit - factor * 3 + factor * 2 - 1) // (factor * 2)
        )

    def count(self):
        count = sum(self.primes)
        assert count == self.known[self.limit]
        return count

    def __str__(self):
        return str(self.count())


def main():
    sieve = Sieve()
    sieve.clear_all()
    print(sieve)


__name__ == '__main__' and main()
