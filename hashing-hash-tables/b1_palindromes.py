#Write an efficient function that checks whether any permutation
#of an input string is a palindrome.

#You can assume the input string only contains lowercase letters.

def can_turn_into_palindrome(input_str):
    if len(input_str) % 2 == 1:
        can_have_char_without_pair = True
    else:
        can_have_char_without_pair = False

    chars_parity_is_even = {}
    #in this one we're tracking if a char is encountered even
    #or odd number of times instead of counting the occurrences
    for char in input_str:
        if char in chars_parity_is_even:
            chars_parity_is_even[char] = True
        else:
            chars_parity_is_even[char] = False
    
    for is_char_even in chars_parity_is_even.values():
        if not is_char_even:
            if can_have_char_without_pair:
                can_have_char_without_pair = False
            else:
                return False

    return True