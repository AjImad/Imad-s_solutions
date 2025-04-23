# problem link: https://www.hackerrank.com/challenges/sherlock-and-anagrams/

from collections import defaultdict

def sherlockAndAnagrams(s):
    pairs = 0
    substr_map = defaultdict(int)
    n = len(s)

    for l in range(1, n):
        for i in range(n-l+1):
            sort_sub = ('').join(s[i:i+l])
            substr_map[sort_sub] += 1

    for count in substr_map.values():
        pairs += count * (count - 1) // 2

    return pairs
