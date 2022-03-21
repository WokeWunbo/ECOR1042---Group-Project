# Arun Karki 101219923

# imports
import T075_P1_book_category_dictionary

# Function 7: get_books_by_publisher
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

# Function 8: get_all_categories_for_book_title
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