nums = [-1,0,3,5,9,12]
target = 9

def search(nums, target):
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1


print(search(nums, target))