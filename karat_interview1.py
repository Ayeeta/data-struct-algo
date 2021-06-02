"""you're given input 12+4 should return the correct result"""

from sympy import * 

def calculate(givenString):
    return str(simplify(givenString))

print(calculate('14+4'))   

print('()')
            