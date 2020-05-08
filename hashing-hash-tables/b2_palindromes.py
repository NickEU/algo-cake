#Write an efficient function that checks whether any permutation
#of an input string is a palindrome.

#You can assume the input string only contains lowercase letters.

def can_turn_into_palindrome(inputStr):
    oddNumbers = set()

    for char in inputStr:
        if char in oddNumbers:
            oddNumbers.remove(char)
        else:
            oddNumbers.add(char)

    return len(oddNumbers) == 1 \
    if len(inputStr) % 2 == 1 else len(oddNumbers) == 0
    


print(can_turn_into_palindrome('civic') == True)
print(can_turn_into_palindrome('c') == True)
print(can_turn_into_palindrome('livci') == False)
print(can_turn_into_palindrome('livcilvc') == True)
print(can_turn_into_palindrome('livcilvd') == False)
print(can_turn_into_palindrome('civil') == False)
print(can_turn_into_palindrome('ivicc') == True)
print(can_turn_into_palindrome('cccvv') == True)

