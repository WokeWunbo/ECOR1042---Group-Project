# Arun Karki 101219923

file = open("google_books_dataset.csv", "r")
next(file)

book_dictionary = {}

# loop for every line in the file
for contents in file:
      
      # make a neat list of every key information into a table ex. ['title', 'author']
      book_information = contents.strip("\n").split(",")
      
      # key info organized as follows: 0 = title, 1 = author, 2 = rating, 3 = publisher, 4 = pages, 5 = category, 6 = language
      category = book_information[5]
      category_book = []
      
      # remove category from book_information so we can add the information in a dictionary without category
      book_information.pop(5) 
      
      # inset all information made of dictionary into list so we can format it in any way we want
      category_book.append({
          "title" : book_information[0],
          "author" : book_information[1],
          "language " : book_information[5],
          "rating" : book_information[2],
          "publisher" : book_information[3],
          "pages" : book_information[4]
          })
      
      # if category key doesn't exist inside book_dictionary, then create one, then add the new book in its appropriate value
      if not book_dictionary.get(category): book_dictionary.update({category : []})
      book_dictionary[category].append(category_book[0])
            
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

      times_looped = 0
      # loop through all keys so we have category for everything
      for category in dictionary.keys():
            # get list of books in every category from dictionary (held as value of key)
            for books_in_category in dictionary.values():
                  for book in books_in_category:
                        times_looped += 1
                        if (book_title == book.get('title')):
                              category_with_book.add(category)

      # loop through all caterogies (filtered by set) and print out result
      for category in category_with_book:
            number_books += 1
            #print(f"Category {number_books}: \"{category}\"")
      
      print("bro i ran", times_looped, "times...")
      return number_books

get_all_categories_for_book_title(book_dictionary, "Antiques Roadkill: A Trash 'n' Treasures Mystery")

file.close()
