from c2_count_words import count_words

count_words_test_cases = {
    'How about a beer?': {'how': 1, 'about': 1, 'a': 1, 'beer': 1},
    'A good day to die': {'good': 1, 'a': 1, 'day': 1, 'to': 1, 'die': 1},
    'The bill came to five dollars.':\
     {'the': 1, 'bill': 1, 'came': 1, 'to': 1, 'five': 1, 'dollars': 1},
     "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake.":\
     {'we': 4, 'came': 1, 'saw': 1, 'conquered': 1, 'then': 1, 'ate': 1, "bill's": 1, 'mille-feuille': 1, 'cake': 1},
     'After beating the eggs, Dana read the next step:':\
     {'after': 1, 'beating': 1, 'the': 2, 'eggs': 1, 'dana': 1, 'read': 1, 'next': 1, 'step': 1},

}

def run_test_suite():        
    for inputS, expectedOutput in count_words_test_cases.items():
        print(count_words(inputS) == expectedOutput)

run_test_suite()