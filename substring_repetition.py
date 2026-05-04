"CSES Problem link: https://cses.fi/problemset/result/17077534/"

s = input()

l = 0
substr_max = 1

for r in range(1, len(s)): # range( 1, len(s))
    if s[r] != s[r-1]:
        l = r
    substr_max = max(r-l+1, substr_max)

print(substr_max)