
import json

# Load the username, if it has been stored previously.
#  Otherwise, prompt for the username and store it.   

filename = 'username.json'  
 
try:
  with open(filename) as f_obj: #  try to open the file username.json. If this file exists, we read the username back into memory
    username = json.load(f_obj) #  and print a message welcoming back the user in the else block.

# If this is the first time the user runs the program, username.json won’t exist and a FileNotFoundError will occur ➌. 
# Python will move on to the except block 
except FileNotFoundError:
  username = input("What is your name? ") # we prompt the user to enter their username.
  with open(filename, 'w') as f_obj: #  json.dump() to store the username
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!") # print a greeting

else:
  print("Welcome back, " + username + "!")
