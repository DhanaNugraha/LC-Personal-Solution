nums = [100,4,200,1,3,2]
# initial idea = sorted nums
#makes a dict to count the consecutive ele (1st sequence: 5 length)
def longestConsecutive(nums):
    sortedNums = sorted(nums)
    print(sortedNums)

    # sequence:length
    outputDict = {}
    sequence = 1

    # counter for each sequence
    count = set()

    for num in sortedNums:
        # adds num to count if its empty or if there is a prev value
        if count == set() or (num-1) in count:
            count.add(num)
            print(count)

        # finish up the sequence and change to another
        else:
            # store count length
            outputDict[sequence] = len(count)
            # change sequence number
            sequence += 1
            # make current num as start for next sequence
            count = {num}
            
    # input last sequence
    outputDict[sequence] = len(count)

    return max(outputDict.values())
    

print(longestConsecutive(nums))