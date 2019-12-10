"""
there are 3 ways
n-1, n-2, n-3
"""
def countways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return countways(n-1) + countways(n-2) + countways(n-3)

print(countways(4))