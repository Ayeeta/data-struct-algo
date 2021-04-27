def multiples(a,b):
    mult = set()
    for i in range(1, 1000):
        x = 3 * i
        if x < 1000:
            mult.add(x)
        j = 5 * i
        if j < 1000:
            mult.add(j)
    s = sum(mult)
    return s


def num_places(x):
    nums = []
    a = 1
    while x != 0:
        y = x % 10
        nums.append(y * a)
        x = x // 10
        a = a * 10
    return sorted(nums, reverse=True)

print(341%10)