from sympy import simplify

def zero(op=None):
    if op != None:
        b=op
        return int(simplify('1'+b))
    return '0'

def one(op=None):
    if op != None:
        b=op
        return int(simplify('1'+b))
    return '1'

def two(op=None):
    if op != None:
        b = op
        return int(simplify('2'+b))    
    return '2'

def three(op=None):
    if op != None:
        b = op
        return int(simplify('3'+b))
    return '3'

def four(op=None):
    if op != None:
        b = op
        return int(simplify('4'+b))
    return '4' 

def five(op=None):
    if op != None:
        b = op
        return int(simplify('5'+b))
    return '5' 

def six(op=None):
    if op != None:
        b = op
        return int(simplify('6'+b))
    return '6' 
def seven(op=None):
    if op != None:
        b = op
        return int(simplify('7'+b))
    return '7'  

def eight(op=None):
    if op!=None:
        b=op
        return int(simplify('8'+b))
    return '8'

def nine(op=None):
    if op != None:
        b = op
        return int(simplify('9'+b))
    return '9'

def plus(num_str):
    return '+{}'.format(num_str)

def minus(num_str):
    return '-{}'.format(num_str)

def times(num_str):
    return '*{}'.format(num_str)

def divided_by(num_str):
    return '/{}'.format(num_str)

print(two(divided_by(three())))

print(two(times(five())))

