"""
Problem: Select Top Scorers
You have n groups, and for each group, participants submit their points one by one. You only consider the last p points entered for each group.
From those p points, select all participants who have the maximum score. If multiple participants share the maximum, select them all.
Input:

First line: two integers n (number of groups) and p (number of points to consider per group)
Next n lines: a series of integers (more than p) representing points — only the last p matter

Output:

Two integers separated by a space:

Total number of selected participants
Sum of their points



Example:
Input:
3 4
10 5 10 3 5 2 7 8
7 7 9 7
2 8 8 1
Output:
4 33
Explanation:

Group 1: last 4 points are 5, 2, 7, 8 → max=8 → 1 selected (8 pts)
Group 2: last 4 points are 7, 7, 9, 7 → max=9 → 1 selected (9 pts)
Group 3: last 4 points are 2, 8, 8, 1 → max=8 → 2 selected (16 pts)
Total: 4 participants, 33 points
"""

n, p = map(int, input().split())

participants = 0
score = 0

for i in range(n):
    group_points = list(map(int, input().split())) # input: 3 4 6 7 ...

    last_p = group_points[-p:]

    max_score = max(last_p)
    count = last_p.count(max(last_p))
    
    participants += count
    score += max_score*count

print(participants, score)


