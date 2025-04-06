#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    a_score = b_score = 0
    
    for ia, ib in zip(a,b):
        if (ia > ib):
            a_score += 1
        elif (ia < ib):
            b_score += 1
    return [a_score, b_score]