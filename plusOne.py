def plus_one(digits):
    last_digit = digits.pop()
    digits.append(last_digit + 1)
    return digits


def plus_one2(digits):
    return [int(x) for x in str(int(str(digits)[1:-1:3])+1)]

# print(plus_one2([4,3,2,1]))

s = [9,4,3,2,1]

def analyze(numbers):
    max = None
    min = None
    result = []
    index = {}
    for n in numbers:
        index[n] = True
        if not max or n > max:
            max = n
        if not min or n < min:
            min = n
    for i in range(min + 1, max):
        if i not in index:
            result.append(i)
    print(index)
    return result

numbers = [3,0,5,9]
print(analyze(numbers))