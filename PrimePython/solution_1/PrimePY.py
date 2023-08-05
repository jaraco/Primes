"""
Python Prime Sieve
"""

import math


class Sieve:
    rawbits: list[bool]
    """Storage for sieve - since we filter evens, just half as many bits"""

    sieveSize: int
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
        self.sieveSize = limit
        self.rawbits = [True] * (int((self.sieveSize + 1) / 2))

    def GetBit(self, index):
        """
        Get a bit from the array of bits, but automatically just filter out
        even numbers as false,
        and then only use half as many bits for actual storage
        """
        # even numbers are automaticallty returned as non-prime
        return self.rawbits[index // 2] if index % 2 else False

    def factors(self):
        factor = 3
        q = math.sqrt(self.sieveSize)
        while factor < q:
            factor = next(filter(self.GetBit, range(factor, self.sieveSize)))
            yield factor
            factor += 2

    def clear_all(self):
        for factor in self.factors():
            self.clear(factor)

    def clear(self, factor):
        # If marking factor 3, skip marking 6 (it's a mult of 2)
        # so start with the 3rd instance of this factor's multiple.
        # Then step by factor * 2 because every second one is going
        # to be even by definition.
        # The for loop to clear the bits is "hidden" in the array slicing.
        self.rawbits[factor * 3 // 2 :: factor] = [False] * (
            (self.sieveSize - factor * 3 + factor * 2 - 1) // (factor * 2)
        )

    def countPrimes(self):
        count = sum(self.rawbits)
        assert count == self.known[self.sieveSize]
        return count

    def __str__(self):
        return str(self.countPrimes())


def main():
    sieve = Sieve()
    sieve.clear_all()
    print(sieve)


__name__ == '__main__' and main()
