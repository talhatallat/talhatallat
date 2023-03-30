# 10-11. Favorite Number: Write a program that prompts for the user’s favorite number. 
# Use json.dump() to store this number in a file. 
# Write a separate program that reads in this value and prints the message, “I know your favorite number! It’s _____.”

# ---------------to store values in the file-------------
import json

filename = 'favorite_number.json'

with open(filename, 'w') as f_obj:
    prompt = input("What is your favorite number?")
    json.dump(prompt, f_obj)

# ---------------to read values from the same file---------------
import json

filename = 'favorite_number.json'

with open(filename) as f_obj:
    read = json.load(f_obj)
    print("I know your favorite number! Its "+ read +".")
    
# 10-12. Favorite Number Remembered: Combine the two programs from Exercise 10-11 into one file. 
# If the number is already stored, report the favorite number to the user. 
# If not, prompt for the user’s favorite number and store it in a file. 
# Run the program twice to see that it works.

import json

filename = 'favorite_number.json'

try:
    with open(filename) as f_obj:
        read = json.load(f_obj)
        
except FileNotFoundError:
    
    with open(filename, 'w') as f_obj:
        prompt = input("What is your favorite number?")
        json.dump(prompt, f_obj)
        print("I will remember your fav no once you come back, " + prompt + "!") # print a greeting

else:
    print("I know your favorite number! Its "+ read +".")

# 10-13. Verify User: The final listing for remember_me.py assumes either that the user has already entered their username or that the program is running for the first time. 
# We should modify it in case the current user is not the person who last used the program.
# Before printing a welcome back message in greet_user(), ask the user if this is the correct username. 
# If it’s not, call get_new_username() to get the correct username.

import json

def greet_user():
    """Greet the user by name."""

    filename = 'username.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)

    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
                
    else:
        user = input("Are you " + username + "? Enter (yes OR no)")
        if user == "yes":
            print("welcome "+ username.title() +"!")
        else: 
            return get_new_username()

def get_new_username():
    """ """
    filename = 'username.json'
    
    username = input("Who are you? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")

greet_user()
