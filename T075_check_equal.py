# Arun Karki 101219923
# Fayez Minai 101233745
# Madi Broadhurst 101222532
# Sean Charlton 101226484

# imports
from T075_P3_sorting_fun import *
from T075_P1_load_data import book_category_dictionary

# Function authors have been commented before every function.

# Function 1 (by Arun Karki 101219923): check_equal
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

# Don't run when importing: all tests for testing all 4 functions
if __name__ == "__main__":
    
    file_name = "google_books_dataset.csv"
    dictionary = book_category_dictionary(file_name)
    total, passes = 0, 0
    
    # sort_books_title
    passes += check_equal(f"{sort_books_title(dictionary)[0].get('title')} appears before {sort_books_title(dictionary)[1].get('title')}", sort_books_title(dictionary)[0].get('title') <= sort_books_title(dictionary)[1].get('title'), True)
    total += 1
    
    # sort_books_publisher
    passes += check_equal(f"{sort_books_publisher(dictionary)[3].get('publisher')} appears before {sort_books_publisher(dictionary)[2].get('publisher')}", sort_books_publisher(dictionary)[3].get('publisher') <= sort_books_publisher(dictionary)[2].get('publisher'), False)
    total += 1
    
    # sort_books_author
    passes += check_equal(f"{sort_books_author(dictionary)[4].get('author')} appears before {sort_books_author(dictionary)[6].get('author')}", sort_books_author(dictionary)[4].get('author') <= sort_books_author(dictionary)[6].get('author'), False)
    total += 1
    
    # sort_books_ascending_rate
    passes += check_equal(f"{sort_books_ascending_rate(dictionary)[0].get('rating')} is greater in rating than {sort_books_ascending_rate(dictionary)[1].get('rating')}", sort_books_ascending_rate(dictionary)[0].get('rating') <= sort_books_ascending_rate(dictionary)[1].get('rating'), True)
    total += 1
    
    print(f"Total Passes: {passes}\nTotal Fails: {total-passes}")