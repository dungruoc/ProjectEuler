# -*- coding: utf-8 -*-
"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Ideas:
1) find out prime numbers under N/2 + 1
2) test if N is devided by any among these prime numbers

"""

def divided_by(iPrimeList, iNumber):
    for num in reversed(iPrimeList):
        if iNumber % num == 0:
            return num
    return 0

def next_prime(iPrimeList):
    aNext = iPrimeList[-1] + 1
    while divided_by(iPrimeList, aNext):
        aNext += 1
    return aNext

def find_factor(iPrimeList, iNumber):
    aFactor = divided_by(iPrimeList, iNumber)
    aLargest = aFactor
    while aFactor > 0:
        iNumber = iNumber/aFactor
        aFactor = divided_by(iPrimeList, iNumber)
        if aFactor > aLargest:
            aLargest = aFactor
    return iNumber, aLargest

def find_largest_factor(iNumber):
    aPrimeList = [2, 3, 5, 7, 11]
    iNumber, aLargest = find_factor(aPrimeList, iNumber)
    while aLargest < iNumber:
        aLimit = iNumber / 2 + 1
        aNextPrime = next_prime(aPrimeList)
        aNewPrime = False
        if aNextPrime <= aLimit:
            aPrimeList.append(aNextPrime)
            aNewPrime = True
        iNumber, aNewLargest = find_factor(aPrimeList, iNumber)
        if not aNewPrime and aNewLargest == 0:
            aNewLargest = iNumber
        if aLargest < aNewLargest:
            aLargest = aNewLargest
    return aLargest
            

def main():
    print('Hello Problem 3')
    print(find_largest_factor(13195))
    print(find_largest_factor(600851475143))

if __name__ == '__main__':
    main()