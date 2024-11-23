
# count prefix product, count suffix product
# answer = prefix[i-1] * suffix[i+1]

nums = [1,2,3,4]

def productExceptSelf(nums):
    # index:product
    prefixProduct = {}
    suffixProduct = {}
    answer = []

    # loop to calc prefix
    for i in range(0, len(nums)):
        if i == 0:
            prefixProduct[i] = nums[i]
        else:
            # uses previous procut calc
            prefixProduct[i] = prefixProduct[i-1] * nums[i]

    # loop to calc suffix
    for i in reversed(range(0, len(nums))):
        if i == (len(nums)-1):
            suffixProduct[i] = nums[i]
        else:
            # uses previous procut calc (the dict key is in descending order)
            suffixProduct[i] = suffixProduct[(i+1)] * nums[i]

    # answer = prefix[i-1] * suffix[i+1]    
    for i in range(0, len(nums)):
        if i == 0:
            answer.append(suffixProduct[i+1])
        elif i == (len(nums)-1):
            answer.append(prefixProduct[i-1])
        else:
            answer.append(prefixProduct[i-1] * suffixProduct[i+1])

    return answer
        

print(productExceptSelf(nums))     

