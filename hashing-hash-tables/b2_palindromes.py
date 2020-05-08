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

    return len(oddNumbers) <= 1

