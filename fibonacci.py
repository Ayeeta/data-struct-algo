def fibonacci_recur(i):
    if i <= 0:
        return "Input incorrect"
    elif i == 1:
        return 0
    elif i == 2:
        return 1
    else:
        return fibonacci_recur(i-1)+ fibonacci_recur(i-2)


print(fibonacci_recur(9))