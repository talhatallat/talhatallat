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

