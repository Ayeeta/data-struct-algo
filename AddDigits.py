def add_digits(num):
    ans = 0
    while num:
        mod = num % 10
        ans += mod
        if ans >= 10:
            ans %= 10
            ans += 1
            num //= 10
    return ans


print(add_digits(38))