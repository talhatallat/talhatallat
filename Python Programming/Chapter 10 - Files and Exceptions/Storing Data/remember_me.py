import json

username = input("What is your name? ") #  prompt for a username to store.

filename = 'username.json'
with open(filename, 'w') as f_obj:
  json.dump(username, f_obj) #  json.dump(), passing it a username and a file object, to store the username in a file
  print("We'll remember you when you come back, " + username + "!") #  print a message informing the user that we’ve stored their information
