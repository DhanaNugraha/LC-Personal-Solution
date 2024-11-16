nums = [-10,7,19,15]
target = 9

# coba dlu ini
# make set()
# cek len(str(target))
# for i in len(nums)
#   if nums[i] in set:
#       continue
#   else:
#       counter


def twoSum(nums, target):
    passed = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in passed:
            return [passed[diff], i]
        else:
            passed[num] = i

print(twoSum(nums, target))