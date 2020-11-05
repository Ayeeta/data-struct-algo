import math

def poseven(n):
    if not n or n < 0:
        return False
    return (math.log10(n)/math.log10(7))%1 == 0