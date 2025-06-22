"""
Problem link: https://www.hackerrank.com/challenges/leonardo-and-prime
"""

import math

def is_prime(n):
    if n <= 1:
        return False

    # 2 is only the even prime number
    if n == 2:
        return True
    
    # all other even numbers are not prime
    if n % 2 == 0:
        return False
    
    # increment by 2 to only loop over odd number
    for i in range(3, int(math.sqrt(n)), 2):
        if n % i == 0:
            return False # Found a divisor, it not a prime number
    
    return True # No divisor fount, it's a prime number

def primeCount(n):
    count = 0
    prod = 1
    candidate = 2

    while True:
        if is_prime(candidate):
            if prod * candidate > n:
                break
            count += 1
            prod *= candidate
        candidate

    return count
