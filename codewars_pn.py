def create_phone_number(n):
    #your code here
    str_list = [str(i) for i in n]
    pn = "".join(str_list)
    return "({0}) {1}-{2}".format(pn[0:3], pn[3:6], pn[6:])

def create_phone_number2(n):
    #your code here
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(create_phone_number2([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))