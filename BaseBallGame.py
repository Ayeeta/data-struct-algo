def baseball(l):
    nl=[]
    for i in range(len(l)):
        if l[i] == "+":
            l[i] = int(l[i]-1)
    return l    

print(baseball(["1","2","+"]))