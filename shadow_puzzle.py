"""
LINK: https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1
"""

def calculate_next_jump():
    w, h = [int(i) for i in input().split()]
    n = int(input())  # maximum number of turns before game over.
    x, y = [int(i) for i in input().split()]

    while True:
        bomb_dir = input()

        # shrink horizontally
        if "U" in bomb_dir:
            y_max = y - 1
        elif "D" in bomb_dir:
            y_min = y + 1
        

        # shrink verticaly
        if "R" in bomb_dir:
            x_min = x + 1
        elif "L" in bomb_dir:
            x_max = x - 1

        x = (x_max + x_min) // 2
        y = (y_max + y_min) // 2

        print(f"{x} {y}")