"""
Introduction
Your parents have challenged you and your sibling to a game of two-on-two basketball. Confident they'll win, they let you score the first couple of points, but then start taking over the game. Needing a little boost, you start speaking in Pig Latin, which is a made-up children's language that's difficult for non-children to understand. This will give you the edge to prevail over your parents!

Instructions
Your task is to translate text from English to Pig Latin. The translation is defined using four rules, which look at the pattern of vowels and consonants at the beginning of a word. These rules look at each word's use of vowels and consonants:

vowels: the letters a, e, i, o, and u
consonants: the other 21 letters of the English alphabet
Rule 1
If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to the end of the word.

For example:

"apple" -> "appleay" (starts with vowel)
"xray" -> "xrayay" (starts with "xr")
"yttria" -> "yttriaay" (starts with "yt")
Rule 2
If a word begins with one or more consonants, first move those consonants to the end of the word and then add an "ay" sound to the end of the word.

For example:

"pig" -> "igp" -> "igpay" (starts with single consonant)
"chair" -> "airch" -> "airchay" (starts with multiple consonants)
"thrush" -> "ushthr" -> "ushthray" (starts with multiple consonants)
Rule 3
If a word starts with zero or more consonants followed by "qu", first move those consonants (if any) and the "qu" part to the end of the word, and then add an "ay" sound to the end of the word.

For example:

"quick" -> "ickqu" -> "ickquay" (starts with "qu", no preceding consonants)
"square" -> "aresqu" -> "aresquay" (starts with one consonant followed by "qu")
Rule 4
If a word starts with one or more consonants followed by "y", first move the consonants preceding the "y"to the end of the word, and then add an "ay" sound to the end of the word.

Some examples:

"my" -> "ym" -> "ymay" (starts with single consonant followed by "y")
"rhythm" -> "ythmrh" -> "ythmrhay" (starts with multiple consonants followed by "y")
"""

def translate(text):
    vowels = ['a', 'e', 'i', 'u', 'o']

    words = text.split() if len(text.split()) > 1 else text.split(",")

    for index, word in enumerate(words):
        # Rule 1
        if (
            word[0] in vowels or
            word.startswith('xr') or
            word.startswith('yt')
        ):
            words[index] = word + 'ay'
    
        # Rule 3
        elif 'qu' in word:
            if word.startswith('qu'):
                words[index] = word[2:] + word[:2] + 'ay'
            else:
                qu_indx = word.index('qu')
                words[index] = word[qu_indx+2:] + word[:qu_indx+2] + 'ay'
    
        # Rule 2 & Rule 4
        elif not word[0] in vowels:
            indx = 1
            for l in word[1:]:
                if not l in vowels and l != 'y':
                    indx += 1
                else:
                    break
            words[index] = word[indx:] + word[:indx] + 'ay'

    return words[0] if len(words) == 1 else " ".join(words)
