# problem link: https://leetcode.com/problems/palindrome-number/

def isPalindrome(x:int)->bool:
    # using string conversion
    # s = str(x)
    # return s == s[::-1]

    original = x
    reversed_num = 0

    while x > 0:
        last_digit = x % 10 # to know the last digit of x
        reversed_num = reversed_num * 10 + last_digit # we multiply by 10 to shift to left
        x = x // 10 # remove the last digit from x

    return original == reversed_num
