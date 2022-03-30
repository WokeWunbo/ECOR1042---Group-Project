# Arun Karki 101219923
# Fayez Minai 101233745
# Madi Broadhurst 101222532
# Sean Charlton 101226484

# imports
from T075_P1_load_data import book_category_dictionary

# Function authors have been commented before every function.

# Function 1 (by Madi Broadhurst 101222532): sort_books_title
def sort_books_title(dictionary : dict) -> list:
    
    """The function returns a list of dicitonaires, each one representing a book and its info.
    It is passed a dictionary to gather the data from. The books should be alhpabetically sorted.

    Certain symbols such as an apostrophe are given precidence over A in this function, meaning
    they will appear before a title starting with 'A' does.
    
    >>>sort_books_title(dictionary)
    [
    {'title': "'Salem's Lot",
      'author': 'Barbara Allan',
      'language ': 'English', 
      'rating': 3.3, 
      'publisher': 'Kensington Publishing Corp.', 
      'pages': 288,
      'category': ['Fiction', 'Detective', 'Mystery']},
      
      ... more entries
      ]
    """
    book_list = dictionary_to_list(dictionary)
    #bubble sort
    n = 0
    
    for i in range(len(book_list)):
        for x in range(0, len(book_list)-i-1) :#Counts down each time from length of list 
            if book_list[x]['title'] > book_list[x+1]['title']: #Switches books' places if needed
                book_list[x]['title'], book_list[x+1]['title'] = book_list[x+1]['title'], book_list[x]['title']
                
    return(book_list)

# Function 2 (by Fayez Minai 101233745): sort_books_publisher
def sort_books_publisher(dictionary : dict)-> list:
    """
    The function returns a list of dictionaries with the books stored in the
    dictionary in alphabetical order accoring to the publisher. In addition, 
    books from the same publisher are stored alphabetically according to the
    title of the book.
    
    """
    list_of_books = dictionary_to_list(dictionary)
        
    # Bubble Sort algorithm
    length = len(list_of_books)
    for i in range(length-1):
        for f in range(length-1-i):
            if list_of_books[f]['publisher'] > list_of_books[f + 1]['publisher']:
                list_of_books[f: f + 2] = list_of_books[f + 1], list_of_books[f]
            elif list_of_books[f]['publisher'] == list_of_books[f + 1]['publisher'] and list_of_books[f]['title'] > list_of_books[f + 1]['title']:
                            list_of_books[f], list_of_books[f + 1] = list_of_books[f + 1], list_of_books[f]            
                
    return list_of_books #returns the list of books with 

# Function 3 (by Arun Karki 101219923): sort_books_author
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
    list_book_data = dictionary_to_list(dictionary)
                
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

# Function 4 (by Sean Charlton 101226484): sort_books_ascending_rate
def sort_books_ascending_rate(dictionary : dict) -> list:
      """
      Function sorts books from dictionary in ascending rating. Returns list
      of books. Books without ratings are moved to the start of the list.
      
      >>> sort_books_ascending_rate(book_category_dictionary('google_books_dataset.csv'))
      book_list=[
      {'title': 'The Guardians: The explosive new thriller from international
      bestseller John Grisham', 'author': 'John Grisham','language ': 'English',
      'rating': False, 'publisher': 'Hachette UK', 'pages': 384},
      {another element},...
      ]
      """
      # create empty list to store books
      book_list = [] 
      # iterate through each dictionary value
      for books in dictionary.values(): 
            # iterate through each list value and append it to book_list
            for book in books: 
                  book_list.append(book)
            # iterate through 0 to length of list
            for book1 in range(len(book_list)):
                  # iterate through the index of book1+1 to length of list
                  for book2 in range(book1+1, len(book_list)):
                        # compare the rating at both indices book1 and book2
                        if book_list[book1]['rating'] > book_list[book2]['rating']:
                              # if the rating of book2 is less than book1 
                              # book2 is moved in front of book1
                              book_list[book1], book_list[book2] = book_list[book2], book_list[book1]            
      return book_list

# Function 5 (by Arun Karki 101219923): dictionary_to_list
def dictionary_to_list(dictionary : dict) -> list:
    """Returns a dictionary thats sorted into a list format used to manipulate/sort data for all books
    
    >>>  dictionary_to_list(book_category_dictionary('google_books_dataset.csv'))
    [{
        'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 
        'author': 'Barbara Allan', 
        'language': 'English', 
        'rating': 3.3, 
        'publisher': 'Kensington Publishing Corp.', 
        'category': ['Mystery', 'Detective', 'Fiction'], 
        'pages': 288
    }, {...}]
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
    
    return list_book_data