# Problem link: https://www.hackerrank.com/challenges/counting-valleys/

def countingValleys(steps, path):
    level = 0
    valleys = 0
    
    for s in range(steps):
        if path[s] == 'U':
            level += 1
            if level == 0:
                valleys += 1
        else:
            level -= 1
    
    return valleys