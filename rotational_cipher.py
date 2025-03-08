"""
Instructions
Create an implementation of the rotational cipher, also sometimes called the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on transposing all the letters in the alphabet using an integer key between 0 and 26. Using a key of 0 or 26 will always yield the same output due to modular arithmetic. The letter is shifted for as many values as the value of the key.

The general notation for rotational ciphers is ROT + <key>. The most commonly used rotational cipher is ROT13.
"""

# Solution: 1
from string import ascii_letters

def rotate(text, key):
    rotate_text = ""

    for letter in text:
        if letter.isalpha():
            base = 0
            if letter.isupper():
                base = 26
            rotate_text += ascii_letters[base + (ascii_letters.index(letter) + key) % 26]
        else:
            rotate_text += letter
    
    return rotate_text

# Solution: 2
def rotate_2(text, key):
    chars = "abcdefghijklmnopqrstuvwxyz" # string containing characters to be replaced
    rotate_chars = chars[key:] + chars[:key] # string containing characters to replace with
    translation_table = str.maketrans(chars + chars.upper(), rotate_chars + rotate_chars.upper())
    return text.translate(translation_table)
