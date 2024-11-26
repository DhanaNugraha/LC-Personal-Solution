temperatures = [73,74,75,71,69,72,76,73]


# initial idea, put temp in stack as [temp, i]
# for every temp, loop the answer list to check if it is higher then any of the temp
# if higher append i-i then answer.pop(value) 
# problem is that the output order is wrong
# mitigate by creating initial [0]*len list


def dailyTemperatures(temperatures):
    # stores in [temp, i]
    stack = []

    # make filled list with 0
    answer = [0] * len(temperatures) 

    for i, temp in enumerate(temperatures):

        # while temperature is higher then rightmost temp in stack, and if stack not empty
        while stack != [] and temp > stack[len(stack) - 1][0]:
            # pop and store values
            checkTemp, checkIndex = stack.pop(len(stack) - 1)
            # insert difference in days to answer
            answer[checkIndex] = (i - checkIndex)

        # append current temp and index to stack
        stack.append([temp, i])    

    return answer
       
print(dailyTemperatures(temperatures))
