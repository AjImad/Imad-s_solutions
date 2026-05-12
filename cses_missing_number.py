n = int(input())
numbers = list(map(int, input().split()))


sum_n = (n * (n + 1) ) // 2
sum_nums = sum(numbers)

print(sum_n - sum_nums)