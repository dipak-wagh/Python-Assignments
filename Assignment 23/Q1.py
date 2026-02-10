# Write a python program to implement a class named BookStore with the following specifications
#   The class should contain two instance variables
#   Name (Book Name)
#   Author (Book Author)
# The class should contain one class variable
# NoofBooks (initialize it to 0)
# Define a constructor (__init__) that accepts Name and Author and initailizes instance variables.
# Inside the constructor. increment the class variable NoOfBooks by 1 whenever a new object is created.
# Implement an instance method
# Display() - should Display book by details in the format
# <BookName> by <Author>. No of books: <NoOfBooks> 

class BookStore:
    NoOfBooks = 0   # Class variable

    def __init__(self, name, author):
        self.Name = name
        self.Author = author
        BookStore.NoOfBooks += 1   # Increment when object is created

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")


# Creating objects
b1 = BookStore("The Alchemist", "Paulo Coelho")
b2 = BookStore("Clean Code", "Robert C. Martin")
b3 = BookStore("Python Crash Course", "Eric Matthes")

# Displaying book details
b1.Display()
b2.Display()
b3.Display()
