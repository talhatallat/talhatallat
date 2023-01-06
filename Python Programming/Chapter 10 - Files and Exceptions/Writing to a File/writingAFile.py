# 10-3. Guest: Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.
filename = gust.txt

with open(filename, w) as file_object:
    ask_user_name = input("My name is: \n")
    file_object.write(ask_user_name)
    
# 10-4. Guest Book: Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. Make sure each entry appears on a new line in the file.
