class Library:                                                              #define a class for the library
    def __init__(self):                                                     #initialize the library with an empty list of books                                             
        self.books = []

    def add_book(self, name):                                               #define a method to add a book to the library
        self.books.append(book)
              
    def delete_book(self, name):                                            #define a method to delete a book from the library
        self.books.remove(book)
    
    def list_books(self):                                                   #define a method to list all books in the library
        for book in self.books:
            print(book)

library = Library()                                                         #create an instance of the Library class
                                                              
print("Welcome to the Library!")

while True:                                                                 #start an infinite loop

    act1 = input("Please, enter the action (add, delete, list, exit): ")    #prompt the user for an action
    if act1 == "add":
        for list, book in enumerate(library.books, start=1):
            print(f"Book {list}: {book}")
        book = input("Enter the book name (title): ")
        library.add_book(book)
        print(f"Book '{book}' added successfully.")

    elif act1 == "list":                                                    #if the user chooses to list books
        for list, book in enumerate(library.books, start=1):
            print(f"Book {list}: {book}")

    elif act1 == "delete":                                                  #if the user chooses to delete a book
        for list, book in enumerate(library.books, start=1):
            print(f"Book {list}: {book}")
        book = input("Enter the book title to delete: ")
        library.delete_book(book)
        print(f"Book '{book}' deleted successfully.")

    elif act1 == "exit":                                                    #if the user chooses to exit the program
        print("Exiting the program.")
        break
    
    else:                                                                   #if the user enters an invalid action
        print("Invalid action. Please try again.")