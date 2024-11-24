test = {1: set(), 2:set()}

test[1].add(1)
print(test)

if 1 in test[1]:
    print('works')
else:
    print('broken')


if 1 in test[1]:
    print('works')
else:
    print('broken')
