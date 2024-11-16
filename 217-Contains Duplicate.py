nums = [1,2,3,1]

def containsDuplicate(nums):
    oneDigit = {}
    twoDigit = {}
    threeDigit = {}
    fourDigit = {}
    fiveDigit = {}

    for i in nums:
        if len(str(i)) == 1:
            if i in oneDigit:
                # print('this is if i ', checker)
                return True
            else:
                oneDigit[i] = True
                # print('this is else i ', checker)
        elif len(str(i)) == 2:
            if i in twoDigit:
                # print('this is if i ', checker)
                return True
            else:
                twoDigit[i] = True
                # print('this is else i ', checker)
        elif len(str(i)) == 3:
            if i in threeDigit:
                # print('this is if i ', checker)
                return True
            else:
                threeDigit[i] = True
                # print('this is else i ', checker)
        elif len(str(i)) == 4:
            if i in fourDigit:
                # print('this is if i ', checker)
                return True
            else:
                fourDigit[i] = True
                # print('this is else i ', checker)
        else:
            if i in fiveDigit:
                # print('this is if i ', checker)
                return True
            else:
                fiveDigit[i] = True
                # print('this is else i ', checker)
    return False

print(containsDuplicate(nums))