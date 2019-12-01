def reverse_bits(n):
    x = bin(n)[2:]
    x = x[::-1]
    zero = ""
    for i in range(32-len(x)):
        zero = zero + "0"
    x = x + zero
    return int(x, 2)


def reverse_bits2(n):
    x = int(str(n)[::-1],2)
    return x


print(reverse_bits2(11111111111111111111111111111101))