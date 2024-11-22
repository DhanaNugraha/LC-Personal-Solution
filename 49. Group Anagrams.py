strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    sortedDict = {}

    for str in strs:
        # just using sorted results in list, join makes it a string
        sortedStr = "".join(sorted(str))
        
        if sortedStr in sortedDict:
            sortedDict[sortedStr] += [str] 

        else:
            sortedDict[sortedStr] = [str]

    # nanti di akhir call out all dict variable dijadiin list
    return list(sortedDict.values())



print(groupAnagrams(strs))