"""
Problem link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
28. Find the Index of the First Occurrence in a String
"""

def strStr(haystack, needle):
    index = haystack.find(needle)

    return -1 if index == -1 else index