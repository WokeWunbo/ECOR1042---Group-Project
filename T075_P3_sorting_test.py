# Arun Karki 101219923

# Testing sort_books_title function written by Madi Broadhurst 101222532

# imports
from T075_P3_sorting import sort_books_title
from T075_P1_load_data import book_category_dictionary

def check_equal(description : str, actual_value, expected_value) -> int:
    
    """Return whether a bool expected value is equal to an actual value. Also check for the type to make sure they match.
    Print wether the test passed or not, and what the test was for. Return 1 for 'true', 0 for 'false'
    
    >>> check_equal("sort_books_title(dictionary)[0] appears before sort_books_title(dictionary)[1]", sort_books_title(dictionary)[0]['title'] <= sort_books_title(dictionary)[1]['title'], True)
    1
    >>> check_equal("sort_books_title(dictionary)[0] appears before sort_books_title(dictionary)[1]", sort_books_title(dictionary)[3]['title'] <= sort_books_title(dictionary)[2]['title'], False)
    1
    >>> check_equal("sort_books_title(dictionary)[0] appears before sort_books_title(dictionary)[1]", sort_books_title(dictionary)[4]['title'] <= sort_books_title(dictionary)[6]['title'], False)
    0
    """
    type_check, value_check = type(actual_value) != type(expected_value), actual_value != expected_value
    
    if type_check: print(f"{description}, Failed: expected ({str(expected_value)}) has type {str(type(expected_value).strip('<class> '))}. Outcome ({str(actual_value)}) has type {str(type(actual_value).strip('<class> '))}")
    elif value_check: print(f"{description}, Failed: expected value was {expected_value}, actual value was {actual_value}")
    else: 
        print(f"{description} has passed!")
        return 1
    
    return 0

# Don't run when importing: all tests for testing sort_books_title
if __name__ == "__main__":
    
    file_name = "google_books_dataset.csv"
    dictionary = book_category_dictionary(file_name)
    total, passes = 0, 0

    passes += check_equal(f"{sort_books_title(dictionary)[0].get('title')} appears before {sort_books_title(dictionary)[1].get('title')}", sort_books_title(dictionary)[0].get('title') <= sort_books_title(dictionary)[1].get('title'), True)
    total += 1
    
    passes += check_equal(f"{sort_books_title(dictionary)[3].get('title')} appears before {sort_books_title(dictionary)[2].get('title')}", sort_books_title(dictionary)[3].get('title') <= sort_books_title(dictionary)[2].get('title'), False)
    total += 1
    
    passes += check_equal(f"{sort_books_title(dictionary)[4].get('title')} appears before {sort_books_title(dictionary)[6].get('title')}", sort_books_title(dictionary)[4].get('title') <= sort_books_title(dictionary)[6].get('title'), False)
    total += 1
    
    print(f"Total Passes: {passes}\nTotal Fails: {total-passes}")