# Arun Karki 101219923
# Fayez Minai 101233745
# Madi Broadhurst 101222532
# Sean Charlton 101226484

# imports
from T075_P3_sorting_fun import *
from T075_P1_load_data import book_category_dictionary
from T075_P2_add_remove_search_dataset import *#add_book, remove_book

# Function authors have been commented before every function.

# Function 1 (by Arun Karki 101219923): display_menu
def display_menu() -> None:
    """Function generates the main menu displayed that specifies all the functions available
    """
    
    # generate the menu UI
    commands = ['L)oad data', 'A)dd book', 'R)emove book', 'G)et books\n\tT)itle R)ate A)uthor P)ublisher C)ategory', 'GCT) Get all Categories for book Title', 'S)ort books\n\tT)itle R)ate P)ublisher A)uthor', 'Q)uit']
    for index in range(1, len(commands)+1):
        print(f"{index}- {commands[index-1]}")   

# Function 2 (by Sean Charlton 101226484): adding_book
def adding_book(dictionary : dict) -> dict:
    """Returns _ after adding a new book into the dataset. Function asks for book information for the book to be added
    
    >>> adding_book(dictionary)
    {
        'Action': [
            {'title': 'test-title', 
            'author': 'test-author', 
            'language ': 'test-language', 
            'rating': 3.3, 
            'publisher': 'test-publisher', 
            'pages': 288}
            ], 
        [...]
    }
    """
    title = input('Enter the title of the book to add: ')
    author = input('Enter the author of the book to add: ')
    rating = input('Enter the rating (1-5) of the book to add: ')
    publisher = input('Enter the publisher of the book to add: ')
    pageCount = input('Enter the page count of the book to add: ')
    genre = input('Enter the genre of the book to add: ')
    language = input('Enter the language of the book to add: ')
    book_info = (title, author, language, publisher, genre, rating, pageCount)
    return add_book(dictionary, (book_info))

# Function 3 (by Sean Charlton 101226484): removing_book
def removing_book(dictionary : dict) -> dict:
    """Returns book dataset dictionary after removing a specified book
    
    >>> removing_book(dictionary)
    {
        'Action': [
            {'title': 'test-title', 
            'author': 'test-author', 
            'language ': 'test-language', 
            'rating': 3.3, 
            'publisher': 'test-publisher', 
            'pages': 288}
            ], 
        [...]
    }
    """
    title = input('Enter name of the book to remove: ')
    category = input('Enter category of the book to remove: ')
    return remove_book(dictionary, title, category)

# Function 4 (by Madi Broadhurst 101222532): getting_book
def getting_book(dictionary : dict):
    """Return book informations given following parameters: Title, Rate, Author, Publisher, Category. 
    """
    print("\nAvailable information to get by: \n\tT)itle \n\tR)ate \n\tA)uthor \n\tP)ublisher \n\tC)ategory")
    g_answer = input("Enter your command here: ")
    g_choice = g_answer.upper()
    if g_choice == 'T':#Gets book by title
        g_title = input("\nEnter book title: ")
        return get_books_by_title(dictionary, g_title)
    elif g_choice == 'R': #Gets books by rate
        g_rate = int(input("\nEnter book rating: "))
        return get_books_by_rate(dictionary, g_rate)
    elif g_choice == 'A': #Gets books by author
        g_author = input("\nEnter book author: ")
        return get_books_by_author(dictionary, g_author)    
    elif g_choice == 'P': #Gets books by publisher
        g_publisher = input("\nEnter book publisher: ")
        return get_books_by_publisher(dictionary, g_publisher) 
    elif g_choice == 'C': #Gets books by category
        g_category = input("\nEnter book category: ")
        return get_books_by_category(dictionary, g_category)
    
# Function 5 (by Arun Karki 101219923): sorting_key    
def sorting_key(dictionary : dict) -> list:
    """Returns a list of sorted books. Sort type is entered as a input and the result is a list of books sorted in that type.
    
    >>> sorting_key(dictionary)
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
    print("How do you want to sort")
    sort_by = input('\tT)itle R)ate P)ublisher A)uthor: ').upper()
    options = ('T', 'R', 'P', 'A')
    # if the options are available then sort the books by whatever is asked
    if sort_by in options:
        result = None
        if sort_by == 'T' : result = sort_books_title(dictionary)
        elif sort_by == 'R' : result = sort_books_ascending_rate(dictionary)
        elif sort_by == 'P' : result = sort_books_publisher(dictionary)
        elif sort_by == 'A' : result = sort_books_author(dictionary)
        return result
        
# Function 6 (by Arun Karki 101219923): UI
def UI() -> None:
    """
    Generate a UI with options to add, remove, get, or sort information from a book dataset
    """    
          
    # booleans set for 'breaking' the while loop and to check if a file has been loaded
    continue_loop = True
    loaded_file = False
    
    # loop while flag is true
    while continue_loop:
        # display the menu each time the loop repeats, set up the available options in the menu
        display_menu()
        options = ('Q', 'L', 'S', 'A', 'R', 'G', 'GCT')
        quit_key, load_key, sort_key, add_key, remove_key, get_key, GCT_key = options
        # if the option is Q (quit) then 'break' the while loop
        request = input('Please type your command: ').upper()
        if request == quit_key: continue_loop = False
        
        # check if file is loaded/loadable and if the request was to load the file
        if not loaded_file and request == load_key:
            file_name = input("Please enter file name: ")
            # NOTE: TAs said no need to error handle if file doesn't exist
            if open(file_name): 
                loaded_file = True
                
        # check if file is loaded before doing any sorting/adding etc...
        if loaded_file:
            # check to see if the request is an available option 
            if request.upper() in options:
                
                dictionary = book_category_dictionary(file_name)
                # adding book
                if request == add_key: adding_book(dictionary)
                # removing book
                elif request == remove_key: removing_book(dictionary)  
                # getting book
                elif request == get_key: getting_book(dictionary)                    
                # get all category
                elif request == GCT_key:
                    title = input("Please enter a book title: ")
                    result = get_all_categories_for_book_title(dictionary, title)    
                # sorting options
                elif request == sort_key: print(sorting_key(dictionary))
                    
            # notify user that an invalid option has been chosen
            else:
                print("No such command")
        # notify user that no file has been loaded so no requests can be made   
        else:
            print("No file loaded")
  
# call the main UI so everything appears when this script is ran      
if __name__ == "__main__":
    UI()