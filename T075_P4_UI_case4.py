# Arun Karki 101219923

# imports
from T075_P3_sorting_fun import *
from T075_P1_load_data import book_category_dictionary

# Function 1: UI
def UI() -> None:
    """
    Generate a UI with options to add, remove, get, or sort information from a book dataset
    """
    
    # generate the menu UI
    commands = ['L)oad data', 'A)dd book', 'R)emove book', 'G)et books\n\tT)itle R)ate A)uthor P)ublisher C)ategory', 'GCT) Get all Categories for book Title', 'S)ort books\n\tT)itle R)ate P)ublisher A)uthor', 'Q)uit']
    def display_menu():
        for index in range(1, len(commands)+1):
            print(f"{index}- {commands[index-1]}")      
            
    # booleans set for 'breaking' the while loop and to check if a file has been loaded
    continue_loop = True
    loaded_file = False
    # loop while flag is true
    while continue_loop:
        # display the menu each time the loop repeats, set up the available options in the menu
        display_menu()
        options = ('Q', 'L', 'S')
        quit_key, load_key, sort_key = options
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
                # all sorting-related options
                if request == sort_key:
                    sort_by = input('\tT)itle R)ate P)ublisher A)uthor: ').upper()
                    options = ('T', 'R', 'P', 'A')
                    # if the options are available then sort the books by whatever is asked
                    if sort_by in options:
                        dictionary = book_category_dictionary(file_name)
                        if sort_by == 'T' : sort_books_title(dictionary)
                        elif sort_by == 'R' : sort_books_ascending_rate(dictionary)
                        elif sort_by == 'P' : sort_books_publisher(dictionary)
                        elif sort_key == 'A' : sort_books_author(dictionary)
            # notify user that an invalid option has been chosen
            else:
                print("No such command")
        # notify user that no file has been loaded so no requests can be made   
        else:
            print("No file loaded")
        
if __name__ == "__main__":
    UI()