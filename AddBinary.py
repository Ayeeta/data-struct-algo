def add_binary(a, b):
    return str(bin(int(a, 2) + int(b, 2)))[2:]

def ret_binary(a):
    return str(bin(int(a,2)))

print(add_binary("1010", "1011"))