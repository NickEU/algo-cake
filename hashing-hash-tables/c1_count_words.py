# Write code that takes a long string and builds
# its word cloud data in a dictionary, where the keys
# are words and the values are the number of times the words occurred.

def count_words(input_str):
    word = ''
    delimeters = ('.', '?', '!', ':', ',', ' ', '(', ')', '"')
    result = {}
    word_is_over = False
    for char in input_str:
        if char in delimeters:
            word_is_over = True
        else:
            if word_is_over:
                insert_word(result, word)
                word_is_over = False                
                word = ''
            word += char
    
    if word != '':
        insert_word(result, word)
    
    return result

def insert_word(result, word):
    word = word.lower()
    if word in result:
        result[word] += 1
    else:
        result[word] = 1



print(count_words('After beating the eggs, Dana read the next step:'))
print(count_words("We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."))
print(count_words('The bill came to five dollars.'))
print(count_words('A good day to die'))
print(count_words('How about a beer?'))