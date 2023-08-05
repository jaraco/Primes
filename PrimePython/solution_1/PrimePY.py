"""
Python Prime Sieve
"""

import math


class prime_sieve(object):
    rawbits: list[bool]
    """Storage for sieve - since we filter evens, just half as many bits"""

    sieveSize: int
    """Upper limit, highest prime we'll consider"""

    primeCounts = {
        10: 4,  # Historical data for validating our results - the number of primes
        100: 25,  # to be found under some limit, such as 168 primes under 1000
        1000: 168,
        10000: 1229,
        100000: 9592,
        1000000: 78498,
        10000000: 664579,
        100000000: 5761455,
    }

    def __init__(this, limit=1000000):
        this.sieveSize = limit
        this.rawbits = [True] * (int((this.sieveSize + 1) / 2))

    def GetBit(this, index):
        """
        Get a bit from the array of bits, but automatically just filter out
        even numbers as false,
        and then only use half as many bits for actual storage
        """
        if index % 2 == 0:  # even numbers are automaticallty returned as non-prime
            return False
        else:
            return this.rawbits[index // 2]

    def runSieve(this):
        factor = 3
        q = math.sqrt(this.sieveSize)

        while factor < q:
            factor = next(filter(this.GetBit, range(factor, this.sieveSize)))

            # If marking factor 3, skip marking 6 (it's a mult of 2)
            # so start with the 3rd instance of this factor's multiple.
            # Then step by factor * 2 because every second one is going
            # to be even by definition.
            # The for loop to clear the bits is "hidden" in the array slicing.
            this.rawbits[factor * 3 // 2 :: factor] = [False] * (
                (this.sieveSize - factor * 3 + factor * 2 - 1) // (factor * 2)
            )

            factor += 2  # No need to check evens, so skip to next odd (factor = 3, 5, 7, 9...)
        return this

    def countPrimes(self):
        count = sum(self.rawbits)
        assert count == self.primeCounts[self.sieveSize]
        return count

    def __str__(self):
        return str(self.countPrimes())


__name__ == '__main__' and print(prime_sieve().runSieve())
