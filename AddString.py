def addString(num1, num2):
    return str(int(num1)+ int(num2))

#Without directly converting to int use eval()

def addString2(a,b):
    return str(eval(a+'+'+b))

print(addString2("5", "4"))