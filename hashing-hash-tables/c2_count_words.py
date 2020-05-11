# Write code that takes a long string and builds
# its word cloud data in a dictionary, where the keys
# are words and the values are the number of times the words occurred.

# Assume the input will only contain words and standard punctuation.

def count_words(input_str):
    result = {}
    word_start_idx = word_length = 0
    delimeters = ('.', '?', '!', ':', ',', ' ', '(', ')', '"')
    for idx, char in enumerate(input_str):
        if not char in delimeters:
            if word_length == 0:
                word_start_idx = idx
            word_length += 1
        else:
            if word_length != 0:
                word = input_str[word_start_idx:word_start_idx + word_length]
                insert_word(result, word)
                word_length = 0
                print(word)
    
    if word_length > 0:
        insert_word(result, input_str[word_start_idx:word_start_idx + word_length])
    
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