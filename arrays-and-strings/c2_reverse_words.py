# Write a function reverseWords() that 
# takes a message as a list of characters
# and reverses the order of the words in place.

# When writing your function, 
# assume the message contains only letters and spaces,
# and all words are separated by one space.
def reverseWords(message):
    result = message
    reverseList(result, 0, len(result) - 1)
    wordStartIdx = idx = 0
    while idx <= len(result):
        if len(result) == idx or result[idx] == ' ':
            reverseList(result, wordStartIdx, idx - 1)
            wordStartIdx = idx + 1
        idx += 1
    print(result)
    return result

def reverseList(list, wordStartPos, wordEndPos):
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