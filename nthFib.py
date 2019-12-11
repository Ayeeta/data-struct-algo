def nthFib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return nthFib(n-2) + nthFib(n-1)