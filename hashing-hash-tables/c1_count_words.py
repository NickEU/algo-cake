# Write code that takes a long string and builds
# its word cloud data in a dictionary, where the keys
# are words and the values are the number of times the words occurred.

def count_words(inputStr):
    word = ''
    delimeters = ('.', '?', '!', ':', ',', ' ', '(', ')', '"')
    result = {}
    wordIsOver = False
    for idx, char in enumerate(inputStr):
        if char in delimeters:
            wordIsOver = True
        else:
            if wordIsOver:
                insert_word(result, word)
                wordIsOver = False                
                word = ''
            word += char
    
    if word != '':
        insert_word(result, word)
    
    return result

def insert_word(result, word):
    lwrCasedWord = word.lower()
    if lwrCasedWord in result:
        result[lwrCasedWord] += 1
    else:
        result[lwrCasedWord] = 1



print(count_words('After beating the eggs, Dana read the next step:'))
print(count_words("We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."))
print(count_words('The bill came to five dollars.'))
print(count_words('A good day to die'))
print(count_words('How about a beer?'))