s = "aab"

def lengthOfLongestSubstring(s):
    left, right = 0, 0
    substring = set()
    output = 0

    while right < len(s):
        print('passed here')
        if s[right] not in substring:
            print(s[right], 'im here')
            substring.add(s[right])
        
        else:
            print(output, substring)
            output = max(output, len(substring))
            left += 1
            right = left
            substring = set()
            continue

        right += 1

    output = max(output, len(substring))

    return output

print(lengthOfLongestSubstring(s))