nums = [1,2,3,1]

def containsDuplicate(nums):
    passed = set()

    for i in nums:
        if i in passed:
            return True
        else:
            passed.add(i)
    return False

print(containsDuplicate(nums))