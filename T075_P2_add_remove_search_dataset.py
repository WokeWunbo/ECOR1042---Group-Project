# Arun Karki 101219923
# Fayez Minai 101233745
# Madi Broadhurst 101222532

# imports
from T075_P1_load_data import book_category_dictionary

# Function authors have been commented before every function.

# Function 1 (by Arun Karki 101219923): add_book
def add_book(dictionary : dict[list], book_info : tuple) -> dict[list]:
    
    """Returns an updated dictionary after adding a new one into the previous dictionary
    
    >>> add_book(T075_P1_book_category_dictionary.book_category_dictionary(file_name), ("TEST-title", "TEST-author", "TEST-language", "TEST-publisher", "Action", "TEST-rating", "TEST-pages"))
    {'Action': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language ': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'TEST-title', 'author': 'TEST-author', 'language ': 'TEST-language', 'rating': 'TEST-rating', 'publisher': 'TEST-publisher', 'pages': 'TEST-pages'}], 'Fiction': [{'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language ': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language ': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226}]}
    """
    # unpack tuple containing book infos
    title, author, language, publisher, category, rating, pages = book_info
    flag = False
    
    # loop through all category till matching category found
    for categories in dictionary:
        if categories == category: 
            # if category doesnt exist, it'll add create a new one
            if not dictionary.get(category): dictionary.update({category : []})
            # add new book info to dictionary
            dictionary[category].append({
                "title" : title,
                "author" : author,
                "language " : language,
                "rating" : rating,
                "publisher" : publisher,
                "pages" : pages
            })
            flag = True
            
    # print statements     
    if flag: print("The book has been added correctly") 
    else: print("There was an error adding the book")
    
    return dictionary

# Function 2 (by Arun Karki 101219923): remove_book
def remove_book(dictionary : dict[list], title : str, category : str) -> dict[list]:
    
    """Returns an updated dictionary after removing a book from matching title and category
    
    >>> remove_book(T075_P1_book_category_dictionary.book_category_dictionary(file_name), "Antiques Roadkill: A Trash 'n' Treasures Mystery", "Action")
    {'Action': [], 'Fiction': [{'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language ': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544}, {'title': 'Edgedancer: From 
    the Stormlight Archive', 'author': 'Brandon Sanderson', 'language ': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226}]}
    """
    # loop throuhg all categories and find category we're looking for
    flag = False
    for categories in dictionary:
        if (categories == category):
            # look for the specific title in the matching category
            for books in dictionary.get(categories):
                # title has been found, pop the book out and turn flag on for print statements
                if books.get("title") == title:
                    dictionary[category].pop()
                    flag = True
    
    # print statements
    if flag: print("The book has been removed correctly")
    else: print("There was an error removing the book. Book not found.")  

    return dictionary
 
# Function 3 (by Madi Broadhurst 101222532): get_books_by_category
def get_books_by_category(dictionary : dict, category : str) -> int:
    
    """Returns and ineteger representing the number of books in a category/genre,
    and prints that integer along with the titles and authors' names of the books 
    in alphabetical order. 
    
    Requires the dictionary from Case 1 where all books are sorted by genre/category, and the
    desired category to gather books from.
    
    >>> get_books_by_category(book_category_dictionary('google_books_dataset.csv'), 'Fiction')
    39
    """
    
    # Defining/Initialising variables used in the function
    books_in_category = set()
    book_total = 0
    i = 0
    
    # Making a set of all the book titles and their authors in the given category 
    for books in dictionary[category]:
        if books != '':
            books_in_category.add((books['title'], books['author']))
            book_total += 1
            
    # Convert the set into a list for alphabetical sorting
    book_list = list(books_in_category)
    book_list.sort()
    
    # Print statement
    print("The category", category , "has" , book_total , "books. This is the list of books:")
    for tuples in book_list :
        print('Book', i+1 , ': "' , book_list[i][0], '" by "' , book_list[i][1], '"' , sep='')
        i += 1
    
    return book_total

# Function 4 (by Madi Broadhurst 101222532): get_books_by_rate
def get_books_by_rate(dictionary: dict, rate: int) -> int:
    
    """Returns and integer representing the number of books with a rating in a certain range,
    and prints that integer along with the titles and authors' names of the coresponding books 
    in alphabetical order. 
    
    Requires the dictionary from Case 1 where all books are sorted by genre/category, and the
    desired rate of the books to be searched for.
    
    The integer passed must be positive, the functino will still run if it is negative, but will
    not yield any useful result.
    
    >>> get_books_by_rate(book_category_dictionary('google_books_dataset.csv'), 3)
    8
    >>> get_books_by_rate(book_category_dictionary('google_books_dataset.csv'), 4)
    67
    >>> get_books_by_rate(book_category_dictionary('google_books_dataset.csv'), -4)
    0
    """
    
    # Defining variables to be used in function
    book_total = 0
    books_with_rate = set()
    i = 0
    
    # Sifting through all of the rates of each of the books
    for category in dictionary:
        for books in dictionary[category]:
            if float(books['rating']) >= rate and float(books['rating']) < rate+1 :
                # Making a set of all the book titles and their authors in the given category 
                if books['rating'] != '':
                    books_with_rate.add((books['title'], books['author']))
                    
    # Convert the set into a list for alphabetical sorting
    book_list = list(books_with_rate)
    book_list.sort()  
    print(book_list)

    # Print statement
    book_total = len(book_list)
    print("There are", book_total , "books whose rating is between" , rate , "and" , rate+1 , ". This is the list of books:")
    for tuples in book_list :
        print('Book', i+1 , ': "' , book_list[i][0], '" by "' , book_list[i][1], '"' , sep='')
        i += 1    
        
    return book_total

# Function 5 (Mohammad Fayez Minai 101233745): get_books_by_title
def get_books_by_title (dictionary: dict, bookname: str) -> bool:
    
    """This function returns true if the inputted book title is in the 
    dictionary
    
    >>> get_books_by_title(dictionary, 'The Mysterious Affair at Styles')
    The book was found   
    True
    >>> get_books_by_title(dictionary, 'The way he did not blah blah')
    Fhe book was NOT found
    False
    """
    
    is_found = False #setting previous for stopping loop
    
    for category in dictionary.keys(): #making loop to find the books from dictionary
        if is_found:
            break
        else :
            list_books = dictionary[category]
            for book in list_books:
                if bookname == book['title']:
                    print ("The book was found")
                    is_found = True
                
    if is_found == False: #To return book was not found if the title is not in dictionary
        print("The book was NOT found")

    return is_found

# Function 6 (Mohammad Fayez Minai 101233745): get_books_by_author
def get_books_by_author (dictionary: dict, author: str) -> int:
    
    """This function finds the amount of books written by an aouthor and it 
    then finds the titles of those books and prints them all out
    
    >>> get_books_by_author(dictionary, 'Agatha Christie')
    The author Agatha Christie has written the following books:
    Book 1: "The Mysterious Affair at Styles" rating: "4.4"
    Book 2: "The Red Signal: An Agatha Christie Short Story" rating: "5.0"
    Book 3: "And Then There Were None" rating: "4.6"
    3. 
    """
    
    books_with_author = set() 
    number_of_books = 0 # Zero number of books currently, added on later
    
    print(f"The author {author} has written the following books:")

    # Finds the books written by author and adds to the empty list
    for categories in dictionary.values():
          for books in categories:
                if author == books.get('author'):
                      books_with_author.add((books['title'], books['rating']))

    # Using the books found adds the number to 0 to find number of boos by author  
    for books in books_with_author:
          number_of_books += 1
          title, rating = books # unpack tuple containing information inside set
          print(f"Book {number_of_books}: \"{title}\" rating: \"{rating}\"")        
    
    return number_of_books

# Function 7 (Arun Karki 101219923): get_books_by_publisher
def get_books_by_publisher(dictionary : dict[list], publisher_name : str) -> int:
      """Return the number of books published by a given publisher and print the book information
      
      >>> get_books_by_publisher(book_dictionary, "Kensington Publishing Corp.")
      2
      >>> get_books_by_publisher(book_dictionary, "Marvel Entertainment")
      6
      >>> get_books_by_publisher(book_dictionary, "Hachette UK")
      12
      """
      
      books_with_publisher = set()
      number_books = 0
      
      print(f"The publisher {publisher_name} has published the following books:")
      
      # get list of books in every category from dictionary (held as value of key)
      for books_in_category in dictionary.values():
            for book in books_in_category:
                  if publisher_name == book.get('publisher'):
                        books_with_publisher.add((book['title'], book['author']))
                        
      # loop through filtered set so no duplicates and we can print out + keep track of number of books
      for book in books_with_publisher:
            number_books += 1
            title, author = book # unpack tuple containing information inside set
            print(f"Book {number_books}: \"{title}\" by \"{author}\"")        
      
      return number_books
  
# Function 8 (Arun Karki 101219923): get_all_categories_for_book_title
def get_all_categories_for_book_title(dictionary : dict[list], book_title : str) -> int:
      """Return number of times a is present in all categories and print the category
      
      >>> get_all_categories_for_book_title(book_dictionary, "Antiques Roadkill: A Trash 'n' Treasures Mystery")
      3
      >>> get_all_categories_for_book_title(book_dictionary, "Deadpool Kills the Marvel Universe")
      1
      >>> get_all_categories_for_book_title(book_dictionary, "Little Girl Lost: A Lucy Black Thriller")
      3
      """
      
      category_with_book = set()
      number_books = 0

      print(f"The book title {book_title} belongs to the following categories:")
      
      # get every key in the dictionary 
      for category in dictionary:
            # check the title of the books stored in category key
            for book in dictionary.get(category):
                  # if title matches, put in set so it filters out duplicates
                  if book.get('title') == book_title:
                        category_with_book.add(category)              
                        
      # loop through all caterogies (filtered by set) and print out result
      for category in category_with_book:
            number_books += 1
            print(f"Category {number_books}: \"{category}\"")

      return number_books
  
# Unit Testing Function (by Madi Broadhurst 101222532): check_equal
def check_equal(description : str, outcome, expected) -> int:
    
    # Returns an integer so that a tally of passed/failed tests can be kept using the return value of the test(as seen commented out below)
    """Returns 1 or 0 based on whether a function passed or failed respectively.
    A funciton will only pass if it produces the same value with the same type as that of the expected.
    
    This function should be passed the description of the function to be tested, along with the actual 
    value it returned and its expected value.
    
    Precondition: This function does not work for testing floats or any data type containing floats. 
    
    >>> check_equal("get_books_by_rate(book_category_dictionary('google_books_dataset.csv'), 3)", 8, 8)
    1
    >>> check_equal("get_books_by_category(book_category_dictionary('google_books_dataset.csv'), 'Fiction')", -39, 39)
    0
    """
    print("\nNow testing:" , description , "\n")
    # Will not continue to test after this if the types are not equal
    if type(outcome) != type(expected): 
        print("TEST FAILED. Expected", expected , "of type" , type(expected) , ". Received" , outcome , "of type" , type(outcome))
        print("----------")
        return 0
    # Will only pass if values are equal
    elif outcome == expected:
        print("TEST PASSED.")
        print("----------")
        return 1
    else:
        print("TEST FAILED. Expected", expected , ", received" , outcome)
        print("----------")
        return 0
    
# Don't run when importing
if __name__ == "__main__":
    
    # variables
    file_name = 'google_books_dataset.csv'
    tests_passed = 0
    
    # Test Case for Function 1:
    tests_passed += check_equal("add_book(book_category_dictionary(file_name), ('TEST-title', 'TEST-author', 'TEST-language', 'TEST-publisher', 'Action', 'TEST-rating', 'TEST-pages'))", 1, 1)
    
    # Test Case for Function 2:
    tests_passed += check_equal("remove_book(book_category_dictionary(file_name), 'Antiques Roadkill: A Trash 'n' Treasures Mystery', 'Action')", 1, 1)

    # Test Case for Function 3:
    tests_passed += check_equal("get_books_by_category(book_category_dictionary(file_name), 'Fiction')", 39, 39)
    
    # Test Case for Function 4:
    tests_passed += check_equal("get_books_by_rate(book_category_dictionary(file_name), 3)", 4, 4)
    
    # Test Case for Function 5:
    tests_passed += check_equal("get_books_by_title(book_category_dictionary(file_name), 'The Mysterious Affair at Styles')", True, True)
    
    # Test Case for Function 6:
    tests_passed += check_equal("get_books_by_author(book_category_dictionary(file_name), 'Agatha Christie')", 2, 2)
    
    # Test Case for Function 7:
    tests_passed += check_equal("get_books_by_publisher(book_category_dictionary(file_name), 'Kensington Publishing Corp.')", 6, 6)
    
    # Test Case for Function 8:
    tests_passed += check_equal("get_all_categories_for_book_title(book_category_dictionary(file_name), 'Antiques Roadkill: A Trash 'n' Treasures Mystery')", 3, 3)
    
    print(tests_passed, "amount of tests passed.")