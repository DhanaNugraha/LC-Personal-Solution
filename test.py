# test = {1: 20, 2:40}
test =[1,2,3,4,5,"+"]
# print(set(test.keys()))
# if 1 in list(test.keys):
#     print('works')

a = str(test[0]) + test[5] + str(test[2])

print(a)


def generateParenthesis(n):
    stack = []
    output = []
    def backtrack (OpenN,ClosedN): 
        if OpenN == ClosedN == n:
            print(1, OpenN, ClosedN)
            # current position is at the end of the decision tree, append result to output
            output.append("".join(stack))
            # return no result to go back to backtrack function in if ClosedN
            return
        if OpenN < n:
            print(2, OpenN, ClosedN)
            stack.append("(")
            # after backtract done, remove the open bracket from stack to finish current backtrack loop
            backtrack(OpenN+1, ClosedN)
            stack.pop()
        if ClosedN < OpenN:
            print(3, OpenN, ClosedN)
            stack.append(")")
            backtrack(OpenN, ClosedN+1)
            # after backtract done, remove the close bracket from stack to finish current backtrack loop
            stack.pop()
    backtrack(0,0)
    return output


print(generateParenthesis(n))