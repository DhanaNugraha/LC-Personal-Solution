# save as index in a set as tuples (i,j,k)?
# save as output given in example
# for in for in for in range full, full -1, full -2
# time limit exceeded
# try sorting and skipping same numbers for i first then j, then k


nums = [-1,0,1,2,-1,-4,-1]

def threeSum(nums):
    # sort the nums for easier skip later
    nums = sorted(nums)
    print(sorted(nums))

    # initial location of pointers
    i = 0
    j = 1
    k = 2

    # stores output in list
    output = []

    # traverse through the nums list as three pointers
    for i in range(0, len(nums) - 2):
        # skip the number if it was previously tested as i
        if i > 0 and nums[i] == nums[i - 1]:
            print(nums[i], nums[i-1], 'i')
            continue

        for j in range(i + 1, len(nums) - 1):
            # skip the number if it was previously tested as j
            if j > (i + 1) and nums[j] == nums[j - 1]:
                print(nums[j], nums[j-1], 'j')
                continue

            for k in range((j + 1), len(nums)):
                # skip the number if it was previously tested as k
                if k > (j + 1) and nums[k] == nums[k - 1]:
                    print(nums[k], nums[k-1], 'k')
                    continue
                print(i, j, k)
                currentSum = nums[i] + nums[j] + nums[k]

                if currentSum == 0:
                    check = sorted((nums[i], nums[j], nums[k]))
                    if check not in output:
                        output.append(check)
                
    return output

print(threeSum(nums))

