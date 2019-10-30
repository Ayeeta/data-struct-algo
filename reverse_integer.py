def reverse_int(n):
    x = 0
    if n > 0:
        strx = str(n)
        x += int(strx[::-1])
    if n == 0:
        return 0
    if n < 0:
        stry = str(n)
        y = stry[1:]
        x += -1 * int(y[::-1])
    max_bit = 2**31-1
    if abs(x) > max_bit:
        return 0
    else:
        return x

print(reverse_int(-10))