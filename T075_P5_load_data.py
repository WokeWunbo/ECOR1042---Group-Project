# Arun Karki 101219923
# Fayez Minai 101233745
# Madi Broadhurst 101222532
# Sean Charlton 101226484
# Written by Arun Karki. Reviewed by Fayez Minai, Madi Broadhurst, Sean Charlton

# Function 1: book_category_dictionary
def book_category_dictionary(file_name : str) -> dict:
      
      """Returns a dictionary that reads into csv file and sorts
      categories as keys and values as the information of the books excluding
      the category.
      
      Precondition: file path may not be found, use r"FILE_PATH" as argument when calling
      
      >>> book_category_dictionary("google_books_dataset.csv")
      book_dictionary = {
            "Fiction":[ {
                        "title": "Antiques Roadkill: A Trash 'n' Treasures Mystery",
                        "author": " Barbara Allan",
                        "language ": "English",
                        "rating": 3.3,
                        "publisher": " Kensington Publishing Corp.",
                        "pages": 288
                        },
                        {another element},
                        ...
                   ]
      """
      
      file = open(file_name, "r")
      next(file) # skip the first line as it contains headers

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
            "rating" : book_information[2] != 'N/A' and float(book_information[2]),
            "publisher" : book_information[3],
            "pages" : int(book_information[4])
            })
            
            # if category key doesn't exist inside book_dictionary, then create one, then add the new book in its appropriate value
            if not book_dictionary.get(category): book_dictionary.update({category : []})
            book_dictionary[category].append(category_book[0])

      file.close()

      # loop through all categories and index all books in that category
      for category in book_dictionary:
            category_books = book_dictionary.get(category)
            # if there's more than 1 book, then there could be re-occuring books
            if len(category_books) > 1:
                  occurences = {}
                  # if a book appears more than once, increment its occurance
                  for books in category_books:
                        title = books.get('title')
                        if occurences.get(title): occurences.update({title : occurences.get(title)+1})
                        # book only appears once
                        else: occurences.update({title : 1})
                  # if the book occured more than once in the previous test, then go through and filter out 
                  if occurences.get(title) > 1:
                        for books in category_books:
                              title = books.get('title')
                              if occurences.get(title) > 1:
                                    # find index of that book, and pop it out
                                    for index in range(occurences.get(title)):
                                          if books in category_books:
                                                category_books.pop(category_books.index(books))         
                                                                                
      return book_dictionary