"""
Problem link: https://leetcode.com/problems/first-unique-character-in-a-string/

Description:

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1. 

"""

from collections import Counter

def firstUniqChar(s: str) -> int:
    freq_map = Counter(s)

    for i, c in enumerate(s):
        if freq_map[c] == 1:
            return i
        
    return -1