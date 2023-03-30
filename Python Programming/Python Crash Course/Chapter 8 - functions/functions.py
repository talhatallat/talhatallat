# Defining a Function

# 8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.
def display_message():
    print("Learning about funsctions in this chapter")
display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.
def favorite_book(book):
    """Display a simple greeting.""" #  docstring, which describes what the function does
    print("My favorite books is " + book.title())
favorite_book('Alice in Wonderland')
