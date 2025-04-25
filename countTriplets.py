# problem link: https://www.hackerrank.com/challenges/count-triplets-1/

from collections import defaultdict

def countTriplets(arr, r):

    left_map = defaultdict(int)
    right_map = defaultdict(int)

    # initialize right_map with all elements frequency
    for item in arr:
        right_map[item] += 1

    triplets = 0

    for j in range(len(arr)):
        b = arr[j]
        right_map[b] -= 1 # to make sure j < k

        a = b//r
        c = b*r

        if b % r == 0 and a in left_map and c in right_map:
            triplets += left_map[a] * right_map[c]

        left_map[b] += 1


    return triplets 