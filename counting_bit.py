import os

def getOneBits(n):
# Write your code here
    binary = []
    while True:    
        rest = n // 2
        reminder = n % 2
        binary.insert(0, reminder)
        n = rest
        if rest == 0:
            break
    print("binary :", binary)
    return binary

getOneBits(13)