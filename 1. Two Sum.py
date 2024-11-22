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
    #Uses dict 
    passed = {}

    # enumerate to use both as key and value in dict
    for i, num in enumerate(nums):
        # rephrase q a+b=c == a = c-b
        diff = target - num

        # we wanna check small in the start, so just check the numbers with stuff we passed, not to the right of the given list.
        if diff in passed:
            return [passed[diff], i]
        else:
            passed[num] = i

print(twoSum(nums, target))