# sort first?
# compare line by line

s = 'hello'
t = 'hello'

def isAnagram(s, t):

    compareOne = {}
    for i in s:
        if i in compareOne:
            compareOne[i] += 1
        else:
            compareOne[i] = 1


    compareTwo = {}
    for i in t:
        if i in compareTwo:
            compareTwo[i] += 1
        else:
            compareTwo[i] = 1

    print(compareOne)
    print(compareTwo)

    if compareOne == compareTwo:
        return True
    else:
        return False
    
print(isAnagram(s,t))
