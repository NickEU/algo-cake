from b0_palindromes import can_turn_into_palindrome as palindrome_func0
from b1_palindromes import can_turn_into_palindrome as palindrome_func1
from b2_palindromes import can_turn_into_palindrome as palindrome_func2

palindromesTestCases = {
    'civic': True,
    'c': True,
    'livci': False,
    'livcilvc': True,
    'livcilvd': False,
    'civil': False,
    'ivicc': True,
    'cccvv': True,
}

def runTestSuite(func):
    print('Running testsuite for:', func.__name__ )
    allTestsHavePassed = True
    for passed, expected in palindromesTestCases.items():
        testPassed = func(passed) == expected
        if not testPassed:
            print('Test with the following input has failed:\n', passed)
            allTestsHavePassed = False

    if allTestsHavePassed:
        print('All tests have passed!')

runTestSuite(palindrome_func0)
runTestSuite(palindrome_func1)
runTestSuite(palindrome_func2)