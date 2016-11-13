# -*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

"""

def test_palindrome(iString):
    return iString == iString[::-1]
    
def find_palindrome():
    aLargest = 0
    for i in reversed(xrange(100, 999)):
        aPalindrome = 0
        for j in reversed(xrange(100, 999)):
            aProduct = i * j
            if test_palindrome(str(aProduct)):
                aPalindrome = aProduct
                break
        if aPalindrome > aLargest:
            aLargest = aPalindrome
    return aLargest

def main():
    print('Hello Problem 4')
    print(find_palindrome())

if __name__ == '__main__':
    main()