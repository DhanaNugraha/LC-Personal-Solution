a = 'hello'
compareOne = {}

for i in a:
    if i in compareOne:
        compareOne[i] += 1
    else:
        compareOne[i] = 1

b = 'hello'
compareTwo = {}

for i in b:
    if i in compareTwo:
        compareTwo[i] += 1
    else:
        compareTwo[i] = 1

print(compareOne)
print(compareTwo)

if compareOne == compareTwo:
    print(True)
else:
    print(False)

