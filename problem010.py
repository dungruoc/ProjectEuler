# -*- coding: utf-8 -*-
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import problem007

def sum_prime(iLimit):
    if iLimit <= 2:
        return 0
    if iLimit == 3:
        return 2
    aPrimeList = [2, 3]
    aSum = 5
    while aPrimeList[-1] < iLimit:
        aNext = problem007.next_prime(aPrimeList)
        if aNext < iLimit:
            aSum += aNext
            aPrimeList.append(aNext)
        else:
            break
    return aSum

def main():
    print('Hello Problem 10')
    print(sum_prime(2000000))

if __name__ == '__main__':
    main()
