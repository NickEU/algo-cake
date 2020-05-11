from b0_palindromes import can_turn_into_palindrome as palindrome_func0
from b1_palindromes import can_turn_into_palindrome as palindrome_func1
from b2_palindromes import can_turn_into_palindrome as palindrome_func2

palindromes_test_cases = {
    'civic': True,
    'c': True,
    'livci': False,
    'livcilvc': True,
    'livcilvd': False,
    'civil': False,
    'ivicc': True,
    'cccvv': True,
}

def run_test_suite(func):
    print('Running testsuite for:', func.__name__ )
    all_tests_have_passed = True
    for passed, expected in palindromes_test_cases.items():
        test_passed = func(passed) == expected
        if not test_passed:
            print('Test with the following input has failed:\n', passed)
            all_tests_have_passed = False

    if all_tests_have_passed:
        print('All tests have passed!')

run_test_suite(palindrome_func0)
run_test_suite(palindrome_func1)
run_test_suite(palindrome_func2)