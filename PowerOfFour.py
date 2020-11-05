import math
def pof(n):
    if not n or n < 0:
        return False
    return (math.log10(n)/math.log10(4))%1 == 0