def repeatString(s,n):
    
    if s =='a':
        return n
    a = s*n
    b = a[0:n+1]    
    return b.count('a')

print(repeatString('ab', 100))
