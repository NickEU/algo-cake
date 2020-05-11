#Write an efficient function that checks whether any permutation
#of an input string is a palindrome.

#You can assume the input string only contains lowercase letters.

def can_turn_into_palindrome(inputStr):
    if len(inputStr) % 2 == 1:
        canHaveCharWithoutPair = True
    else:
        canHaveCharWithoutPair = False

    charCounts = {}
    for char in inputStr:
        if char in charCounts:
            charCounts[char] += 1
        else:
            charCounts[char] = 1
    
    for count in charCounts.values():
        if count % 2 == 1:
            if canHaveCharWithoutPair:
                canHaveCharWithoutPair = False
            else:
                return False

    return True