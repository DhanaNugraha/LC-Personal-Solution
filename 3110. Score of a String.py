# print(ord('h'))
s = "zaz"

def scoreOfString(s):
    score = 0
    for i in range(0, len(s) - 1):
        score  += abs(ord(s[i]) - ord(s[i+1]))
    return score

print (scoreOfString(s))