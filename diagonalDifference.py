"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1 + 5 + 9 = 15
The right-to-left diagonal = 3 + 5 + 9 = 17
Their absolute difference is |15 - 17| 2

Function description

Complete the  function with the following parameter:

int arr[n][m]: a 2-D array of integers
Return

int : the absolute difference in sums along the diagonals
"""

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

def diagonalDifference(arr):
    n = len(arr)
    left_to_right_sum = 0
    right_to_left_sum = 0

    for i in range(n):
        left_to_right_sum += arr[i][i]
        right_to_left_sum += arr[i][n-1 - i]

    return abs(left_to_right_sum - right_to_left_sum)

