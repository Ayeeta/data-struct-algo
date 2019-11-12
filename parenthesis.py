#simpler problem
def parenthesis_problem(s):
    left = 0
    for p in s:
        if p == "(":
            left += 1
        if p == ")":
            left -= 1
    if left == 0:
        return "Valid"
    else:
        return "Invalid"


print(parenthesis_problem(")((()))("))