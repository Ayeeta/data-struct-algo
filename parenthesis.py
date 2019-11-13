#simpler problem - assume starting open parenthesis
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


# print(parenthesis_problem(")((()))("))

def parenthesis_problem2(s):
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []
    for i in s:
        if i in open_par:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
        else:
            return False
    return stack == []

print(parenthesis_problem2("{()}"))
