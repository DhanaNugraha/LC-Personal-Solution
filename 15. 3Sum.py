# save as index in a set as tuples (i,j,k)?
# save as output given in example
# for in for in for in range full, full -1, full -2
# time limit exceeded
# try sorting and skipping same numbers for i first then j, then k


nums = [0,0,0]

def threeSum(nums):
    # sort the nums for easier skip later
    nums = sorted(nums)

    # initial location of pointer
    i = 0

    # stores output in list
    output = []

    # traverse through the nums list as three pointers
    for i in range(0, len(nums) - 2):
        # skip the number if it was previously tested as i
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # j and k will be a left and right two pointers
        j = i + 1
        k = len(nums) - 1

        while j < k:
            currentSum = nums[i] + nums[j] + nums[k]

            if currentSum > 0:
                k -= 1

                # keep moving k if the number have already been evaluated
                while nums[k] == nums[k + 1] and j < k:
                    k -= 1
            
            elif currentSum < 0:
                j += 1
                print(j)
                # keep moving k if the number have already been evaluated
                while nums[j] == nums[j - 1] and j < k:
                    j += 1
            
            else:
                # append values that results to 0
                output.append(sorted([nums[i], nums[j], nums[k]]))

                # finish evaluation by moving j 
                j += 1

                # keep moving k if the number have already been evaluated
                while j > (i + 1) and nums[j] == nums[j - 1] and j < k:
                    j += 1

    return output

print(threeSum(nums))

