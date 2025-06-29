"""
Problem link: https://leetcode.com/problems/plus-one/
"""

def plusOne(digits):
    n = len(digits)

    for i in reversed(range(n)):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        
        digits[i] = 0

    # if we exit the loop that mean all the digits are 0 ([0] * n)
    return [1] + [0] * n