"""
Introduction
You work for a company that sells fonts through their website. They'd like to show a different sentence each time someone views a font on their website. To give a comprehensive sense of the font, the random sentences should use all the letters in the English alphabet.

They're running a competition to get suggestions for sentences that they can use. You're in charge of checking the submissions to see if they are valid.

Instructions
Your task is to figure out if a sentence is a pangram.

A pangram is a sentence using every letter of the alphabet at least once. It is case insensitive, so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).

For this exercise, a sentence is a pangram if it contains each of the 26 letters in the English alphabet.
"""

def is_pangram(sentence):
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    
    for l in alphabet:
        if not l in sentence.lower():
            return False

    return True