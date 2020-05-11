#Write an efficient function that checks whether any permutation
#of an input string is a palindrome.

#You can assume the input string only contains lowercase letters.

def can_turn_into_palindrome(input_str):
    odd_numbers = set()

    for char in input_str:
        if char in odd_numbers:
            odd_numbers.remove(char)
        else:
            odd_numbers.add(char)

    return len(odd_numbers) <= 1

