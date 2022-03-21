# Arun Karki 101219923

# Test for Function 5
def check_bool_equal(description : str, call_function : callable, arguments : tuple, expected_value : bool) -> bool: 
    """Return whether a bool expected value is equal to an actual value. Also check for the type to make sure they match.
    Print wether the test passed or not, and what the test was for.
    
    >>> check_bool_equal("After Anna", T075_P2_fun.get_books_by_title, (T075_P1_book_category_dictionary.book_category_dictionary("google_books_dataset.csv"), "After Anna"), True)
    True
    >>> check_bool_equal("After Anna", T075_P2_fun.get_books_by_title, (T075_P1_book_category_dictionary.book_category_dictionary("google_books_dataset.csv"), "After Anna"), 35)
    False
    >>> check_bool_equal("After Anna", T075_P2_fun.get_books_by_title, (T075_P1_book_category_dictionary.book_category_dictionary("google_books_dataset.csv"), "After Anna"), False)
    False
    >>> check_bool_equal("Bring Me Back", T075_P2_fun.get_books_by_title, (T075_P1_book_category_dictionary.book_category_dictionary("google_books_dataset.csv"), "Bring Me Back"), True)
    True
    """
    
    actual_value = call_function(arguments[0], arguments[1])
    value_check, type_check = expected_value == actual_value, type(expected_value) == type(actual_value)
    result = value_check and type_check
    
    if result: print(f"Expected Value: {expected_value}, Actual Value: {actual_value}")
    
    if not value_check: print(f"Expected Value: {expected_value}, did not match, Actual Value: {actual_value}")
    elif not type_check: print(f"Expected Type: {type(expected_value)}, did not match, Actual Type: {type(actual_value)}")
            
    dummy_var = (result and print(f"Test for {description} passed.")) or (not result and print(f"Test for {description} failed."))
    
    return result

# Test for Function 6
def check_int_equal(description : str, call_function : callable, arguments : bool, expected_value : int) -> bool: 
    """Return whether an int expected value is equal to an actual value. Also check for the type to make sure they match.
    Print wether the test passed or not, and what the test was for.
    
    >>> check_bool_equal("Dale Carnegie", T075_P2_fun.get_books_by_author, (T075_P1_book_category_dictionary.book_category_dictionary("google_books_dataset.csv"), "Dale Carnegie"), 2)
    False
    >>> check_bool_equal("Dale Carnegie", T075_P2_fun.get_books_by_author, (T075_P1_book_category_dictionary.book_category_dictionary("google_books_dataset.csv"), "Dale Carnegie"), 1)
    True
    >>> check_bool_equal("Stephen King", T075_P2_fun.get_books_by_author, (T075_P1_book_category_dictionary.book_category_dictionary("google_books_dataset.csv"), "Stephen King"), 1)
    True
    >>> check_bool_equal("Stephen King", T075_P2_fun.get_books_by_author, (T075_P1_book_category_dictionary.book_category_dictionary("google_books_dataset.csv"), "Stephen King"), "Hi")
    False
    """
    
    actual_value = call_function(arguments[0], arguments[1])
    value_check, type_check = expected_value == actual_value, type(expected_value) == type(actual_value)
    result = value_check and type_check
    
    if result: print(f"Expected Value: {expected_value}, Actual Value: {actual_value}")
    
    if not value_check: print(f"Expected Value: {expected_value}, did not match, Actual Value: {actual_value}")
    elif not type_check: print(f"Expected Type: {type(expected_value)}, did not match, Actual Type: {type(actual_value)}")
            
    dummy_var = (result and print(f"Test for {description} passed.")) or (not result and print(f"Test for {description} failed."))
    
    return result