def repeatString(s,n):
    a = s*n
    b = a[0:n+1]
    if b.count('a') == n:
        return n
    return b.count('a')

print(repeatString('ab', 100))
