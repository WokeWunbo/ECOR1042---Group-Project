# Function 7: get_books_by_publisher
def get_books_by_publisher(dictionary, publisher_name):
      
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

#get_books_by_publisher(book_dictionary, "Kensington Publishing Corp.")

# Function 8: get_all_categories_for_book_title
def get_all_categories_for_book_title(dictionary, book_title):

      category_with_book = set()
      number_books = 0

      print(f"The book title {book_title} belongs to the following categories:")

      # loop through all keys so we have category for everything
      for category in dictionary.keys():
            # get list of books in every category from dictionary (held as value of key)
            for books_in_category in dictionary.values():
                  for book in books_in_category:
                        if (book_title == book.get('title')):
                              category_with_book.add(category)

      # loop through all caterogies (filtered by set) and print out result
      for category in category_with_book:
            number_books += 1
            print(f"Category {number_books}: \"{category}\"")

      return number_books

get_all_categories_for_book_title(book_dictionary, "Antiques Roadkill: A Trash 'n' Treasures Mystery")