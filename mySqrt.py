"""
Problem link: https://leetcode.com/problems/sqrtx/
description:
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""

def mySqrt(x):
    #using binary search
    #square root of x is y where y*y<=x
    #possible values for y are within [0, x] non-negative range

    left = 0  #lower bound, square root of 0 is always 0
    right = x #upper bound is x, because square root is always never greater than x, it could be equal or less than x

    res = 0

    while left <= right:
        mid = (left+right) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
            res = mid
        else:
            right = mid - 1

    return res