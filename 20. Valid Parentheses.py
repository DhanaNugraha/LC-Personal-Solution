s = "]"


# initial idea = counting doesnt work because "[(]) is false"
# second idea: make dict to connect open and close parentheses
#  make list to add open parentheses first
#  del open paren from back to front when close paren show up
# if open paren != close paren, false
# return true at the end

def isValid(s):
    # connect close bracket to open bracket
    bracketDict = {")":"(", "]":"[", "}":"{"}

    # Store set of open bracket to call for if statement later
    openBracketSet = set(bracketDict.values())
   
    # store open bracket during iteration
    openBracketList = []
    
    for bracket in s:
        if bracket in openBracketSet:
            # stores open bracket in list
            openBracketList.append(bracket)

        else:
            # if there is no open bracket to check for
            if openBracketList == []:
                return False
            
            # checks if last item in list connects to current closed bracket
            if openBracketList[len(openBracketList) - 1] == bracketDict[bracket]:
                # remove from list if connects
                openBracketList.pop(len(openBracketList) - 1)
        
            else:
                return False
    
    # if there is still leftover open bracket
    if openBracketList != []:
        return False
        
    return True

print(isValid(s))