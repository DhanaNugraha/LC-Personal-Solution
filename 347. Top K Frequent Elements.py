nums = [1,1,1,2,2,3]
k = 2

# dict stores ocurrences
# for k times, find key with max value then insert to list. pop the key-value pair from dict.


def topKFrequent(nums, k):
    # dict to calc appearance
    counter = {}
    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    print(counter)
    
    # change dict to separate key values list for easy access to call keys from value
    counterKeys = list(counter.keys())
    counterValues = list(counter.values())

    output = []
    for i in range (k):
        # get index of max value in the list
        maxIndex = counterValues.index(max(counterValues))

        # use the index to get key
        print(counterKeys[maxIndex])
        output.append(counterKeys[maxIndex])

        # remove from both list to prevent reappearance
        counterKeys.pop(maxIndex)
        counterValues.pop(maxIndex)

    return output

print(topKFrequent(nums, k))