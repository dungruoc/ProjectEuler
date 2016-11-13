# -*- coding: utf-8 -*-
"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

"""

def sum_squares(iNumber):
    aSum = 0
    for num in xrange(1, iNumber + 1):
        aSum += num ** 2
    return aSum

def diff_sums(iNumber):
    aSum = iNumber * (iNumber + 1) / 2
    return (aSum ** 2) - sum_squares(iNumber)

def main():
    print('Hello Problem 6')
    print(diff_sums(100))

if __name__ == '__main__':
    main()
