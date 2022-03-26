# Arun Karki 101219923

# imports
from T075_P1_book_category_dictionary import book_category_dictionary

# Function 1: sort_books_author
def sort_books_author(dictionary : dict) -> list:
    
    """Return a list of books with book being sorted in alphabetic order using author's name. Will also filter repeating books and
    add book with all its categories.
    
    Precondition: file path may not be found, use r"FILE_PATH" as argument when calling
    
    >>> sort_books_author(book_category_dictionary("google_books_dataset.csv"))
    [
        {'title': 'Twas The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit This is Going to Hurt', 
        'author': 'Adam Kay', 
        'language': 'English', 
        'rating': 4.7, 
        'publisher': 'Pan Macmillan', 
        'category': ['Humor'], 
        'pages': 112}, 
        
        {'title': 'The Red Signal: An Agatha Christie Short Story',
        'author': 'Agatha Christie',
        'language': 'English',
        'rating': 5.0,
        'publisher': 'HarperCollins UK', 
        'category': ['Detective', 'Fiction', 'Traditional', 'Mystery'],
        'pages': 40}
    ]
    """
    
    # contains all books
    list_book_data = []
    
    # loop through all book data by key
    for category in dictionary:
        for books in dictionary.get(category):
            
            # same book could appear twice, check to see if this book previously exists before proceeding
            duplicate_found = False
            for book_data in list_book_data:
                if book_data.get('title') == books.get('title'): duplicate_found = True

            if not duplicate_found:
                # get all categories for same book
                category_with_book = set()
                # get every key in the dictionary 
                for matching_category in dictionary:
                    # check the title of the books stored in category key to see if it matches with the book we're looking (w/ same category)
                    for matching_book in dictionary.get(matching_category):
                            # if title matches, put in set so it filters out duplicates, we've found same book with 2 different categories
                            if matching_book.get('title') == books.get('title'): category_with_book.add(matching_category)    
                                      
                # transform set into list and append all info to list
                list_book_data.append({
                    "title" : books.get('title'),
                    "author" : books.get('author'),
                    "language" : books.get('language '),
                    "rating" : books.get('rating'),
                    "publisher" : books.get('publisher'),
                    "category" : list(category_with_book),
                    "pages" : books.get('pages'),
                })       
                
    # Bubble Sort Algorithm with books
   
    # retrieve all authors name and put them in a list to use for sorting book
    all_authors = []
    for book in list_book_data: all_authors.append(book.get('author'))

    # loop for all books in list
    for book in list_book_data:
        # start at index 1 and increment so 1-1 can be indexed as positon 0, etc...
        for counter in range(1, len(all_authors)):
            # find the author's name, and find the book associated with the name
            element = all_authors[counter]
            element_book = list_book_data[counter]
             # index from 1 to 0, 2 to 1, 3 to 1, positions, etc...
            for index in range(counter-1, counter):
                # check to see if current element is 'less' than the next position element
                next_element = all_authors[index]
                next_element_book = list_book_data[index]
                # element is 'smaller' than the next, so swap book positions
                if element < next_element: 
                    all_authors[counter] = next_element
                    all_authors[index] = element
                    list_book_data[counter] = next_element_book
                    list_book_data[index] = element_book
                # if the same author is found, check to see the 'hiercharchy' of the book titles
                elif element == next_element and list_book_data[counter].get('title') < list_book_data[index].get('title'):
                    # make the 'lower' title be first, and 'higher' title to be first
                    list_book_data[counter] = next_element_book
                    list_book_data[index] = element_book
                              
    return list_book_data