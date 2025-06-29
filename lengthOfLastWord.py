"""
Problem link: https://leetcode.com/problems/length-of-last-word/description/
"""

def lengthOfLastString(s:str) -> int:
    return len(s.strip().split()[-1])