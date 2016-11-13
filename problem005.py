# -*- coding: utf-8 -*-
"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

Solution:
This number should be represented by:
p1^k1 * p2^k2 * ....

where p1, p2 are prime numbers from 1 to 20, and the ki satisfies that
all of factor pi^ki <= 20

"""
import problem003

def prime_list(iLimit):
    if iLimit < 2:
        return []
    aPrimeList = [2]
    while aPrimeList[-1] < iLimit:
        aNext = problem003.next_prime(aPrimeList)
        if aNext <= iLimit:
            aPrimeList.append(aNext)
        else:
            break
    return aPrimeList

def least_divisible(iLimit):
    aPrimeList = prime_list(iLimit)
    aFactorList = []
    if aPrimeList:
        for num in aPrimeList:
            aFactor = num
            while aFactor < iLimit:
                aFactor = aFactor * num
            if aFactor > iLimit:
                aFactor = aFactor / num
            aFactorList.append(aFactor)
        return reduce(lambda x, y: x * y, aFactorList)
    return 0

def main():
    print('Hello Problem 5')
    print(least_divisible(20))

if __name__ == '__main__':
    main()
