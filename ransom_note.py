# Problem link: https://www.hackerrank.com/challenges/ctci-ransom-note/

# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):

    mag_map = {} # initialize hashMap that will store key(word) and value(count on the magazine sentence)

    # store magazine as dictionary
    for mag_word in magazine:
        if mag_word in mag_map:
            mag_map[mag_word] += 1
        else:
            mag_map[mag_word] = 1

    for word in note:
        # check if note's word already exist on magazine and at least appears once
        if mag_map.get(word, 0) > 0:
            mag_map[word] -= 1
        else:
            print('No')
            return
        
    print('Yes')
    
