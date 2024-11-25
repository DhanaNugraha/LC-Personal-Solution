tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]


# initial idea, basically same as leetcode 20 valid parentheses
#  if number add to stack, if operator then operate and add back to stack
# use int(equation) to floor down division

def evalRPN(tokens):
    operator = {"+", "-", "*", "/"}
    stack = []

    for token in tokens:
        # separate all operator
        if token == "+":
            calc = stack.pop(len(stack)-2) + stack.pop(len(stack)-1)
            # put back result to stack
            stack.append(calc)

        elif token == "-":
            calc = stack.pop(len(stack)-2) - stack.pop(len(stack)-1)
            stack.append(calc)

        elif token == "*":
            calc =stack.pop(len(stack)-2) * stack.pop(len(stack)-1)
            stack.append(calc)
        
        elif token == "/":
            # without float usually works normally but not in leetcode. we have to change to float to get decimals in calc first and then floor it back using int in leetcode
            calc = float(stack.pop(len(stack)-2)) / float(stack.pop(len(stack)-1))
            # to round down the division
            stack.append(int(calc))
        
        else:
            # put numbers to stack in int form
            stack.append(int(token))

    return stack[0]


print(evalRPN(tokens))

