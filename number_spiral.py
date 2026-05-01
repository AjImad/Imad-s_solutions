# CSES problem link: https://cses.fi/problemset/task/1071


t = int(input())

for i in range(t):
    # y => rows
    # x => columns
    y, x = map(int, input().split())

    layer = max(y, x)

    # check either layer is odd or even
    if not layer % 2: 
        # layer is even
        if layer == y:
            print(layer**2 - (x - 1))
        else:
            print((layer - 1)**2 + y)
    else:
        # layer is odd
        if layer == y:
            print((layer - 1)**2 + x)
        else:
            print(layer**2 - (y - 1))