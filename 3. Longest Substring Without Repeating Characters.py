s = "aab"

def lengthOfLongestSubstring(s):
    left = 0
    substring = set()
    output = 0

    for right in range(len(s)):
        while s[right] in substring:
            substring.remove(s[left])
            left += 1
        
        substring.add(s[right])
        output = max(output, len(substring))

    return output

print(lengthOfLongestSubstring(s))