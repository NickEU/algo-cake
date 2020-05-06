# Write a function that takes a list of characters
# and reverses the letters in place
def reverseLetters(inputList):
    midPointIdx = len(inputList) / 2 
    for currIdx, currChar in enumerate(inputList):
        if midPointIdx <= currIdx:
            break
        temp = currChar
        idxToSwap = - 1 - currIdx
        inputList[currIdx] = inputList[idxToSwap]
        inputList[idxToSwap] = temp
    return inputList


print(reverseLetters(['a', 'b', 'c', 'd']) == ['d', 'c', 'b', 'a'])
print(reverseLetters(['a']) == ['a'])
print(reverseLetters(['k', 'l', 'm', 'n', 'o']) == ['o', 'n', 'm', 'l', 'k'])