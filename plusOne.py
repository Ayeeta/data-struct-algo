def plus_one(digits):
    last_digit = digits.pop()
    digits.append(last_digit + 1)
    return digits


def plus_one2(digits):
    return [int(x) for x in str(int(str(digits)[1:-1:3])+1)]

print(plus_one2([4,3,2,1]))

s = [9]
print(int(str(s)[1:-1:3])+1)