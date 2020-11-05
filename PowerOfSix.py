import math
def pos(n):
    if not n or n < 0:
        return False
    return (math.log10(n)/math.log10(6))%1 == 0