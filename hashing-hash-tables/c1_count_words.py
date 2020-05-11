# Write code that takes a long string and builds
# its word cloud data in a dictionary, where the keys
# are words and the values are the number of times the words occurred.

def count_words(inputStr):
    word = ''
    delimeters = ('.', '?', '!', ':', ',', ' ', '(', ')', '"')
    result = {}
    wordIsOver = False
    for idx, char in enumerate(inputStr):
        if char in delimeters and idx < len(inputStr) - 1:
            wordIsOver = True
        else:
            if wordIsOver or idx == len(inputStr) - 1:
                lwrCasedWord = word.lower()
                if lwrCasedWord in result:
                    result[lwrCasedWord] += 1
                else:
                    result[lwrCasedWord] = 1
                wordIsOver = False                
                word = ''

            word += char
    
    print(result)


count_words('After beating the eggs, Dana read the next step:')
count_words("We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake.")
count_words('The bill came to five dollars.')