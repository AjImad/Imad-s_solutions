# CSES problem link: https://cses.fi/problemset/task/1092/

n = int(input())

som = n*(n+1) // 2

if som % 2 != 0:
    print("NO")

else:
    target = som // 2
    s1 = []
    s2 = []
    remaining = target # track remaining sum needed - recomputation

    for i in range(n, 0, -1):
        if i <= remaining:
            s1.append(i)
            remaining -= i # O(1) update instead of sum(s1)
        else:
            s2.append(i)


    print("YES")
    print(len(s1))
    print(*s1)
    print(len(s2))
    print(*s2)
