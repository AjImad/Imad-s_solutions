"""
Instructions
Determine if a word or phrase is an isogram.

An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:

lumberjacks
background
downstream
six-year-old
"""

import re

def is_isogram(string):
    string = re.sub(r'[ -]', '', string.lower())
    return len(set(string)) == len(string)