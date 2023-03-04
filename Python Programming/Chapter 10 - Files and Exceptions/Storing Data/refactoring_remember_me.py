

import json

def get_stored_username(): #  This function retrieves a stored username and returns the username if it finds one.
  """Get stored username if available."""
  filename = 'username.json'
  try:
    with open(filename) as f_obj:
      username = json.load(f_obj)
  except FileNotFoundError: #  If the file username.json doesn’t exist, the function returns None
    return None 
  else:      
    return username


def greet_user():
  """Greet the user by name."""
  username = get_stored_username() #  print a welcome back message to the user if the attempt to retrieve a username was successful, 
  if username:
    print("Welcome back, " + username + "!") # 
  else: # # and if it doesn’t, we prompt for a new username.
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
      json.dump(username, f_obj)
      print("We'll remember you when you come back, " + username + "!")
      
greet_user()
