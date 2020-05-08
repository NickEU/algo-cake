#Write an efficient function that checks whether any permutation
#of an input string is a palindrome.

#You can assume the input string only contains lowercase letters.

def can_turn_into_palindrome(inputStr):
    if len(inputStr) % 2 == 1:
        canHaveCharWithoutPair = True
    else:
        canHaveCharWithoutPair = False

    charsParityIsEven = {}
    #in this one we're tracking if a char is encountered even
    #or odd number of times instead of counting the occurrences
    for char in inputStr:
        if char in charsParityIsEven:
            charsParityIsEven[char] = True
        else:
            charsParityIsEven[char] = False
    
    for isCharEven in charsParityIsEven.values():
        if not isCharEven:
            if canHaveCharWithoutPair:
                canHaveCharWithoutPair = False
            else:
                return False

    return True


print(can_turn_into_palindrome('civic') == True)
print(can_turn_into_palindrome('c') == True)
print(can_turn_into_palindrome('livci') == False)
print(can_turn_into_palindrome('livcilvc') == True)
print(can_turn_into_palindrome('livcilvd') == False)
print(can_turn_into_palindrome('civil') == False)
print(can_turn_into_palindrome('ivicc') == True)
print(can_turn_into_palindrome('cccvv') == True)

