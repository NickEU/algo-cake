# Write a function that takes a list of characters
# and reverses the letters in place
def reverse_letters(inputList):
    firstIdx = 0
    lastIdx = len(inputList) - 1
    while firstIdx < lastIdx:
        inputList[firstIdx], inputList[lastIdx] \
        = inputList[lastIdx], inputList[firstIdx]
        firstIdx += 1
        lastIdx -= 1
    return inputList


print(reverse_letters(['a', 'b', 'c', 'd']) == ['d', 'c', 'b', 'a'])
print(reverse_letters(['a']) == ['a'])
print(reverse_letters(['k', 'l', 'm', 'n', 'o']) == ['o', 'n', 'm', 'l', 'k'])