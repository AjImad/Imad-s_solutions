# Problem link: https://www.hackerrank.com/challenges/repeated-string/

def repeatedString(s, n):
    count_a_in_s = s.count('a')

    complete_repetitions = n // len(s)

    remainder = n % len(s)

    total_a = complete_repetitions * count_a_in_s

    total_a += s[:remainder].count('a')

    return total_a