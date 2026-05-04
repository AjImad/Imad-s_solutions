n = int(input())

lines = []
line_map = {} # old_line -> new_line

for i in range(n):
    line = input()
    lines.append(line.split())

    old_line = int(lines[i][0])
    new_line = (i+1)*10

    line_map[old_line] = new_line

    lines[i][0] = str(new_line) # renumbering line

    # correct the GOTO/GOSUB lines as well
    for j in range(len(lines[i])):
        if lines[i][j] in ("GOTO", "GOSUB"):
            target = int(lines[i][j+1])
            lines[i][j+1] = str(line_map[target])

for i in range(n):
    print(" ".join(lines[i]))
