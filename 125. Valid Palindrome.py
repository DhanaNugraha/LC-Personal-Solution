s = "0P"

# make a set for all alphabet and numbers


def isPalindrome(s):
    # immediately return true because 1 value in string is always palindrome
    if len(s) == 1:
        return True
    
    # alphabet set 
    alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    # word list
    word = []

    # remove symbols and empty spaces from given string
    for str in s:
        if str.lower() in alphabet:
            word.append(str.lower())
    print(word)

    # using left and right pointer to traverse the given string
    left = 0
    right = len(word) -1

    # stopper for pointers
    difference = right - left
    
    # loop using pointers for the word
    while difference > 0:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
        difference = right - left

    return True
   

print(isPalindrome(s))