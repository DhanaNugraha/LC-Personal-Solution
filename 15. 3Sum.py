# save as index in a set as tuples (i,j,k)?
# save as output given in example
# for in for in for in range full, full -1, full -2
# time limit exceeded


nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    # initial location of pointers
    left = 0
    right = len(nums) - 1

    # stores output in list
    output = []

    # traverse nums as two pointers
    for left in range(0, len(nums) - 1):
        for right in range(left + 1, len(nums)):

            # find in nums for final value to result sum 0. pop to ensure we do not check for same index.
            leftValue = nums.pop(left)
            rightValue = nums.pop(right - 1)

            # last value = 0 - i - j
            find = - leftValue - rightValue

            if find in nums:
                # for checking if it already exist in output
                check = sorted([leftValue, rightValue, find])

                if check not in output:
                    output.append(check)

            # insert values back to nums
            nums.insert(left, leftValue)
            nums.insert(right, rightValue)

    return output

print(threeSum(nums))

