# sort first?
# compare line by line

s = 'hello'
t = 'hello'

# tldr, we count how many ocurrences per letter on each given string

def isAnagram(s, t):

    # using dict to count number of appearance of letter in string s
    compareOne = {}
    for i in s:
        if i in compareOne:
            compareOne[i] += 1
        else:
            compareOne[i] = 1


    # using dict to count number of appearance of letter in string t
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
