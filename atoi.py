def within_range(x):
    min_a = -2**31
    max_a = 2**31-1
    if x > max_a:
        return max_a
    if x < min_a:
        return min_a
    return x
        
def myAtoi(a):
    a = a.strip()
    
    if a[0].isalpha():
        return 0
    else:
        x = [i for i in a.split()]
        return within_range(int(x[0]))


print(myAtoi("91283472332"))



