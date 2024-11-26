temperatures = [73,74,75,71,69,72,76,73]


# initial idea, put temp in stack as [temp, i]
# for every temp, loop the answer list to check if it is higher then any of the temp
# if higher append i-i then answer.pop(value) 
# problem is that the output order is wrong
# mitigate by creating initial [0]*len list
# tries pushing only index


def dailyTemperatures(temperatures):
    # stores in [i]
    stack = []

    # make filled list with 0
    answer = [0] * len(temperatures) 

    for index in range(len(temperatures)):
        # while temperature is higher then last temp in stack, and if stack not empty
        while stack != [] and temperatures[index] > temperatures[stack[-1]]:
            # pop and store value of index
            checkIndex = stack.pop(-1)
            # insert difference in days to answer
            answer[checkIndex] = (index - checkIndex)

        # append current index to stack
        stack.append(index)    

    return answer
       
print(dailyTemperatures(temperatures))
