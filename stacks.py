#Evaluate postfix expression in a stack

def postfix_expr(strs):
    stack_ = []
    math_operators = "+-/*"
    for i in strs:
        if i.isdigit():
            stack_.append(i)
        if i in math_operators:
            b = stack_.pop()
            a = stack_.pop()
            if i == "+":
                stack_.append(int(a) + int(b))
            if i == "-":
                stack_.append(int(a) - int(b))
            if i == "/":
                stack_.append(int(a) / int(b))
            if i == "*":
                stack_.append(int(a) * int(b))
    return stack_[len(stack_)-1]



def postfix_expr2(strs):
    stack_ = []
    math_operators = "+-/*"
    for i in strs:
        if i.isdigit():
            stack_.append(i)
        if i in math_operators:
            b = stack_.pop()
            a = stack_.pop()
            stack_.append(str(eval(a + i + b)))
    return stack_[len(stack_)-1]
            
        


print(postfix_expr2("2 3 1 * + 9 -"))


