"""

Introduction
Raindrops is a slightly more complex version of the FizzBuzz challenge, a classic interview question.

Instructions
Your task is to convert a number into its corresponding raindrop sounds.

If a given number:

is divisible by 3, add "Pling" to the result.
is divisible by 5, add "Plang" to the result.
is divisible by 7, add "Plong" to the result.
is not divisible by 3, 5, or 7, the result should be the number as a string.
"""

def convert(n):
    res = ""
    
    if n % 3 == 0:
        res += "Pling"
    if n % 5 == 0:
        res += "Plang"
    if n % 7 == 0:
        res += "Plong"
    
    return res or str(n)