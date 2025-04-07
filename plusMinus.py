"""
Problem Link: https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true

Given an array of integers, calculate the ratios of its elements that are , , and . Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example

There are  elements: two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

0.400000
0.400000
0.200000
Function Description

Complete the  function with the following parameter(s):

: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.
"""

def plusMinus(arr):
    n = len(arr)
    zero_count = sum(1 for x in arr if x == 0)
    positive_count = sum(1 for x in arr if x > 0)
    negative_count = sum(1 for x in arr if x < 0)

    print(f"{positive_count:.6f}")
    print(f"{negative_count:.6f}")
    print(f"{zero_count:.6f}")