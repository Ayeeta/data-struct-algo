import math

def pot(n):
    if not n or n<0:
        return False
    return (math.log10(3)/math.log10(3))%1 == 0

print(pot(0))