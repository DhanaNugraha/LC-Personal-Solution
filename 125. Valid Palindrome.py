s = "a."

# using str.isalpha() to check for letter, 
# using two pointer to get value from left and right
# change approach, remove all non alphanumeric first??


def isPalindrome(s):
    # using left and right pointer to traverse the given string
    left = 0
    right = len(s) -1

    # stopper for pointers
    difference = right - left
    s = list(s)
    print(s)
    print(difference)

    # # if  len 1 and not empty or not letter return false
    # if (len(s) == 1 and s[0] != " ") or (len(s) == 1 and s[0].lower() == False):
    #     return False

    if len(s) == 1:
        return True

    # false if only 1 value and it is not a letter
    if len(s) == 2 and s[left].lower() != s[right].lower():
        return False

    # loops until pointers meet in the center
    while difference > 1:

        # skips non letters on left pointer
        print(left, right, '0')
        while s[left].isalpha() == False and difference > 1:
            print(left, right, '1')
            left += 1
            # print(left, difference)
        
        # skips non letters on right pointer
        while s[right].isalpha() == False and difference > 1:
            print(left, right, '2')
            right -= 1

        # return false if left and right value not equals
        if s[left].lower() != s[right].lower():
            print(left, right ,'at false')
            print(s[left].lower(), s[right].lower())
            return False
        
        # shift pointers to center and refresh difference
        print(left, right ,'3')
        left += 1
        right -= 1
        print(left, right, '4')
        difference = right - left
    
    return True

print(isPalindrome(s))