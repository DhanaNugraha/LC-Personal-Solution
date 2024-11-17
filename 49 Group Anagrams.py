strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    sortedDict = {}

    for str in strs:
        sortedStr = "".join(sorted(str))
        # sort and combine the strings
        if sortedStr in sortedDict:
            sortedDict[sortedStr] += [str] 
            # print('1',sortedDict)
        else:
            sortedDict[sortedStr] = [str]
            # print('2',sortedDict)
    return list(sortedDict.values())


# nanti di akhir call out all dict variable dijadiin list
print(groupAnagrams(strs))