# Arun Karki 101219923

# imports
import T075_P1_book_category_dictionary

# Function 7: get_books_by_publisher
def get_books_by_publisher(dictionary : dict[list], publisher_name : str):
      """Return the number of books published by a given publisher and print the book information
      
      >>> get_books_by_publisher(book_dictionary, "Kensington Publishing Corp.")
      The publisher Kensington Publishing Corp. has published the following books:
      Book 1: "Antiques Roadkill: A Trash 'n' Treasures Mystery" by "Barbara Allan"
      Book 2: "Antiques Knock-Off" by "Barbara Allan"
      >>> get_books_by_publisher(book_dictionary, "Marvel Entertainment")
      Book 1: "Ultimate Spider-Man Vol. 11: Carnage" by "Brian Michael Bendis"
      Book 2: "Immortal Hulk Vol. 1: Or Is He Both?" by "Al Ewing"
      Book 3: "Spider-Man: Anti-Venom" by "Dan Slott"
      Book 4: "Venomized" by "Cullen Bunn"
      Book 5: "Deadpool Kills the Marvel Universe" by "Cullen Bunn"
      Book 6: "Spider-Verse: Volume 1" by "Dan Slott"
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
def get_all_categories_for_book_title(dictionary : dict[list], book_title : str):
      """Return number of times a is present in all categories and print the category
      
      >>> get_all_categories_for_book_title(book_dictionary, "Antiques Roadkill: A Trash 'n' Treasures Mystery")
      The book title Antiques Roadkill: A Trash 'n' Treasures Mystery belongs to the following categories:
      Category 1: "Mystery"  
      Category 2: "Fiction"  
      Category 3: "Detective"
      >>> get_all_categories_for_book_title(book_dictionary, "Deadpool Kills the Marvel Universe")
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

# delete below part, not needed for submission !

# Get book_dictionary
file_name = "google_books_dataset.csv"
book_dictionary = T075_P1_book_category_dictionary.book_category_dictionary(file_name)

# Test Call Function 8
get_all_categories_for_book_title(book_dictionary, "Deadpool Kills the Marvel Universe")