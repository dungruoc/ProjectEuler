# -*- coding: utf-8 -*-
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?

"""

def divided_by(iPrimeList, iNumber):
    for num in iPrimeList:
        if iNumber % num == 0:
            return num
    return 0

def next_prime(iPrimeList):
    aNext = iPrimeList[-1] + 2
    while divided_by(iPrimeList, aNext):
        aNext += 2
    return aNext

def find_prime(iNth):
    aPrimeList = [2, 3, 5, 7, 11, 13]
    while iNth > len(aPrimeList):
        aNext = next_prime(aPrimeList)
        aPrimeList.append(aNext)
    return aPrimeList[iNth - 1]

def main():
    print('Hello Problem 7')
    print(find_prime(10001))

if __name__ == '__main__':
    main()
