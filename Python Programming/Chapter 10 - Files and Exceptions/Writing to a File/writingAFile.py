# 10-3. Guest: Write a program that prompts the user for their name. 
# When they respond, write their name to a file called guest.txt.
filename = 'guest.txt'

with open(filename, 'w') as file_object:
    ask_user_name = input("My name is: \n")
    file_object.write(ask_user_name)
    
# 10-4. Guest Book: Write a while loop that prompts users for their name. 
# When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. 
# Make sure each entry appears on a new line in the file.
filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    x = True
    while x:
        ask_user_name = input("My name is: \n")
        
        if ask_user_name != 'quit':
            print("Welcome " + ask_user_name +"!")
            file_object.write(ask_user_name+"\n")
        else:
            break
            
# 10-5. Programming Poll: Write a while loop that asks people why they like programming. 
# Each time someone enters a reason, add their reason to a file that stores all the responses.
filename = 'guest_book.txt'

with open(filename, 'a') as file_object: # 'a' Appends to a File (meaning adds to a exiting data stores within a file)
    while True:
        ask_user = input("Why do you like programming? \n")
        
        if ask_user != 'quit':
            file_object.write(ask_user+"\n")
        else:
            break   
