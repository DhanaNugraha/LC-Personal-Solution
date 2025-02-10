# print(ord('h'))
s = "zaz"

def scoreOfString(s):
    score = 0
    for i in range(1, len(s)):
        score  += abs(ord(s[i]) - ord(s[i-1]))
    return score

print (scoreOfString(s))