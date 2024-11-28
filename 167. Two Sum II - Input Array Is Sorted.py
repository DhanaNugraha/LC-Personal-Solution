numbers = [2,7,11,15] 
target = 9

# if target < current , move right
# if target > current, move left

def twoSum(numbers, target):
    # using two pointers
    left = 0
    right = len(numbers) - 1

    while left < right:
        # store current sum
        currentSum = numbers[right] + numbers[left]

        # return index values if target is found
        if target == currentSum:
            return[left + 1, right + 1]
        
        elif target < currentSum:
            right -= 1

        elif  target > currentSum:
            left += 1


print(twoSum(numbers, target))
