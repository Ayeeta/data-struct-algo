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

#using eval()

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

#Balanced parenthesis
def balanced_parenthesis(parenthesis):
    stack_ = []
    open_p = "[{("
    dict_p = {")":"()","}":"{}","]":"[]"}
    if parenthesis[0] in open_p:
        return "unbalanced"
    else:
        for p in parenthesis:
            if p in open_p:
                stack_.append(p)
            else:
                if dict_p[p] == (stack_[len(stack_)-1] + p):
                    stack_.pop()
                else:
                    return "Unbalanced"
        if len(stack_) == 0:
            return "balanced"
        else:
            return "Unbalanced"

#balanced parenthesis 2 - matching based on positiions

# Python3 code to Check for  
# balanced parentheses in an expression 
open_list = ["[","{","("] 
close_list = ["]","}",")"] 
  
# Function to check parentheses 
def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
            

#print(balanced_parenthesis("){}{})(][]"))
print(check("){}{})(][]"))
        