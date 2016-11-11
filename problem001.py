# -*- coding: utf-8 -*-
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all
the multiples of 3 or 5 below 1000.

Input: N
- multiples of 3: 3, 6, ...
  sum3(N): 3*(1+...+N/3) = 3 * (N/3+1) * N/3 / 2

- multiples of 5: 5, 10, ...
  sum5(N): 5*(1+...+N/5)

- excluding multiples of 3 and 5: 15, 30, ...
  sum30(N): 15*(1+...+N/15)

result: sum3 + sum5 - sum30
"""

def sum_multiples(iLimit, iFactor):
    if iLimit > 0 and iFactor > 0:
        aLast = iLimit/iFactor
        return iFactor * aLast * (aLast + 1) / 2
    return 0

def solution(iLimit):
    N = iLimit - 1
    return sum_multiples(N, 3) + sum_multiples(N, 5) - sum_multiples(N, 15)

def main():
    print('Hello Problem 1')
    print(solution(1000))

if __name__ == '__main__':
    main()