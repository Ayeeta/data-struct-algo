import math

def judgeSquareSum(c):
    sq = int(c**0.5)
    ht = {}
    for i in range(sq+1):
        if i**2 == c or c - i**2 in ht or 2*i**2 == c:
            return True
        ht[i**2] = ht.get(i**2, True)
    return False
	

print(judgeSquareSum(5))