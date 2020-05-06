from b2_reverse_letters_list import reverseLetters
# Write a function reverseWords() that 
# takes a message as a list of characters
# and reverses the order of the words in place.

# When writing your function, 
# assume the message contains only letters and spaces,
# and all words are separated by one space.
def reverseWords(message):
    result = reverseLetters(message)
    result.append(' ')
    word = ''
    wordStartIdx = 0
    for idx, el in enumerate(message):
        if el != ' ':
            word += el
        else:
            wordLen = len(word)
            reverseWord(result, wordStartIdx, wordStartIdx + wordLen - 1)
            wordStartIdx += wordLen + 1
            word = ''
    result.pop()  
    return result

def reverseWord(list, wordStartPos, wordEndPos):
    while wordStartPos < wordEndPos:
        list[wordStartPos], list[wordEndPos] \
        = list[wordEndPos], list[wordStartPos]
        wordStartPos += 1
        wordEndPos -= 1



msgInput = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]
msgOutput = ['s', 't', 'e', 'a', 'l', ' ',
             'p', 'o', 'u', 'n', 'd', ' ',
              'c', 'a', 'k', 'e']
print(reverseWords(msgInput) == msgOutput)
msgInput2 = ['g', 'r', 'e', 'a', 't', ' ', 'i', 's', ' ', 'g', 'o', 'd']
msgOutput2 = ['g', 'o', 'd', ' ', 'i', 's', ' ', 'g', 'r', 'e', 'a', 't']
print(reverseWords(msgInput2) == msgOutput2)        
msgInput3 = ['a', ' ', 'b', ' ', 'c', ' ', 'd']
msgOutput3 = ['d', ' ', 'c', ' ', 'b', ' ', 'a']
print(reverseWords(msgInput3) == msgOutput3)
print(reverseWords(['a']) == ['a'])
print(reverseWords(['a', 'b']) == ['a', 'b'])