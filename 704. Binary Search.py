nums = [-1,0,3,5,9,12]
target = 9

def search(nums, target):
    left, right = 0, len(nums) - 1
    
    # nums can be 1
    while left <= right:
        # int division to floor
        mid = (left + right) // 2
        curNum = nums[mid]

        if curNum == target:
            return mid

        elif curNum < target:
            left = mid + 1
        
        else:
            right = mid - 1
            
    return -1



print(search(nums, target))