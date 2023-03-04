import json

filename = 'numbers.json'
with open(filename) as f_obj: #  open file in read mode
  numbers = json.load(f_obj) #  json.load() function to load the information stored in numbers.json file, and store it in the variable numbers.

print(numbers)
