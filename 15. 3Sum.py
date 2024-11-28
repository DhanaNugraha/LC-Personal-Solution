# save as index in a set as tuples (i,j,k)?
# save as output given in example
# for in for in for in range full, full -1, full -2
# time limit exceeded


nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    # initial location of pointers
    i = 0
    j = 1
    k = 2

    # stores output in list
    output = []

    # traverse through the nums list as three pointers
    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range((j + 1), len(nums)):
                print(i, j, k)
                currentSum = nums[i] + nums[j] + nums[k]

                if currentSum == 0:
                    check = sorted((nums[i], nums[j], nums[k]))
                    if check not in output:
                        output.append(check)
                
    return output

print(threeSum(nums))

