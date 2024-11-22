nums = [1,2,3,1]

def containsDuplicate(nums):
    #set is the fastest to loop into compared to dict and list
    passed = set()

    for i in nums:
        if i in passed:
            #Duplicate defo in set
            return True
        else:
            passed.add(i)
    return False

print(containsDuplicate(nums))