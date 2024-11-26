n = 3

# Uses a decision tree 
# conditions:
# 1. if open = closed = n, put to output
# 2. if open is still less than n, add an open bracket
# 3. if closed still less than open, add a closed

def generateParenthesis(n):
    stack = []
    output = []

    def decisionTree(openBracket, closedBracket):

        if openBracket == closedBracket == n:
            # current position is at the end of the decision tree, append result to output
            output.append("".join(stack))
            # technically no need but cuts a bit of time as it doesnt need to pass the rest of the code to finish 
            return
        
        if openBracket < n:
            stack.append("(")
            # after backtract done, remove the open bracket from stack to finish current backtrack loop
            decisionTree(openBracket + 1, closedBracket)
            stack.pop()

        if closedBracket < openBracket:
            stack.append(")")
            # after backtract done, remove the close bracket from stack to finish current backtrack loop
            decisionTree(openBracket, closedBracket + 1)
            stack.pop()
    
    # calls function to run
    decisionTree(0,0)
    return output

print(generateParenthesis(n))
