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
    passed = set()

    for i in range(len(nums)):
        if nums[i] in passed:
            continue
        else:
            counter = i+1
            while counter != len(nums):
                if nums[counter] in passed:
                    counter += 1 
                    print('here 1')
                else:
                    total = nums[i] + nums[counter]
                    print('this is total ', total)
                    if total == target:
                        print('here 3')
                        return [i, counter]
                    else:
                        counter += 1     
                        print('here 4')          
        passed.add(nums[i])
        print('here 5')

print(twoSum(nums, target))