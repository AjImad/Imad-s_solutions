"""
Instructions
The ISBN-10 verification process is used to validate book identification numbers. These normally contain dashes and look like: 3-598-21508-8

ISBN
The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only). In the case the check character is an X, this represents the value '10'. These may be communicated with or without hyphens, and can be checked for their validity by the following formula:

(d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.
"""

import re

def is_valid(isbn):
    isbn = re.sub('-', '', isbn)
    index = 10
    som = 0

    if len(isbn) != 10:
        return False
    
    if 'X' in isbn and isbn.index('X') != 9:
        return False
    
    for n in isbn:
        if not n.isnumeric() and n != 'X':
            return False
        som += (int(n) if n != 'X' else 10) * index
        index -= 1
    
    return som % 11 == 0