# -*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

"""

def test_palindrome(iString):
    return iString == iString[::-1]
    
def find_palindrome_product(iDigit):
    aRange = xrange(10 ** (iDigit - 1), 10 ** iDigit)
    aLargest = 0
    for i in reversed(aRange):
        aPalindrome = 0
        for j in reversed(aRange):
            aProduct = i * j
            if test_palindrome(str(aProduct)):
                aPalindrome = aProduct
                break # No need to loop for j anymore
        if aPalindrome > aLargest:
            aLargest = aPalindrome
    return aLargest

def main():
    print('Hello Problem 4')
    print(find_palindrome_product(3))

if __name__ == '__main__':
    main()