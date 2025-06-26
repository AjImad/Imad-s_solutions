def reverse(x: int) -> int:

    n = abs(x)

    reverse_num = 0

    while n > 0:
        digit = n % 10
        reverse_num = reverse_num * 10 + digit
        n = n // 10

    reverse_num = reverse_num if x > 0 else -1 * reverse_num

    if reverse_num < -2**31 or reverse_num > 2**31 -1:
        return 0
    
    return reverse_num