# imports
import T075_P1_book_category_dictionary

# Main Script

# Function 1
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
    
# Function 2:
def remove_book(dictionary : dict[list], title : str, category : str) -> dict[list]:
    """Returns an updated dictionary after removing a book from matching title and category
    
    >>> remove_book(T075_P1_book_category_dictionary.book_category_dictionary(file_name), "Antiques Roadkill: A Trash 'n' Treasures Mystery", "Action")
    
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

# Calling Function book_category_dictionary
file_name = "test.csv"
dictionary = T075_P1_book_category_dictionary.book_category_dictionary(file_name)
title = "Antiques Roadkill: A Trash 'n' Treasures Mystery"
category = "Action"
#book_info = ("TEST-title", "TEST-author", "TEST-language", "TEST-publisher", "Action", "TEST-rating", "TEST-pages")
#print(add_book(dictionary, book_info))
print(remove_book(dictionary, title, category))