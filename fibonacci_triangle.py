n = int(input())

# ---- SOLUTION 1 ----
# fib = [1, 1]

# for i in range(2, n):
#     fib.append(fib[-1]+fib[-2])

# for r in range(1, n+1):
#     print(*fib[:r])


# ---- SOLUTION 2 ----

a, b = 1, 1

for r in range(1, n+1):
    a, b = 1, 1 
    for i in range(r):
        print(a, end=" ")
        a, b = b, a + b
    print()