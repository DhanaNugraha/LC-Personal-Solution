nums = [3,1,2]


def findMin(nums):
    output = nums[0]
    l, r = 0, len(nums)-1

    while l<=r: 
        if nums[l] <= nums[r]: 
            return min(output, nums[l])
        m = (l+r)//2
        output = min(output, nums[m])
        if nums[m] >= nums[l]:
            l = m+1
        else:
            r = m-1
    return output

            
print(findMin(nums))