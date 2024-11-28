s = "0P"

# make a set for all alphabet and numbers


def isPalindrome(s):
    # immediately return true because 1 value in string is always palindrome
    if len(s) == 1:
        return True

    # word list
    word = []

    # remove symbols and empty spaces from given string
    for str in s:
        if str.isalnum() == True:
            word.append(str.lower())

    # using left and right pointer to traverse the given string
    left = 0
    right = len(word) -1
    
    # loop using pointers for the word
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True
   

print(isPalindrome(s))