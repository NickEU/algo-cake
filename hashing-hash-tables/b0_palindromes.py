#Write an efficient function that checks whether any permutation
#of an input string is a palindrome.

#You can assume the input string only contains lowercase letters.

def can_turn_into_palindrome(input_str):
    if len(input_str) % 2 == 1:
        can_have_char_without_pair = True
    else:
        can_have_char_without_pair = False

    char_counts = {}
    for char in input_str:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    for count in char_counts.values():
        if count % 2 == 1:
            if can_have_char_without_pair:
                can_have_char_without_pair = False
            else:
                return False

    return True