def decrypt_pwd(s):
    numbers=['1','2','3','4','5','6','7','8','9']
    num=[]
    pos=[]
    for i in range(0, len(s)):
        if s[i] in numbers:
            num.append(s[i])
        elif s[i] == '0':
            pos.append(i)
    if len(num) == len(pos):
        num.reverse()
        for i in pos:
            s[i] = num[i]
               

    print(num)
    print(pos)
    

decrypt_pwd("43hcc0a0")