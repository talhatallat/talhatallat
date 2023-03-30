import json #  import the json module
numbers = [2, 3, 5, 7, 11, 13] #  list of numbers

filename = 'numbers.json' # filename to store the list of numbers
with open(filename, 'w') as f_obj: #  open the file in write mode, allowing json to write the data to the file
    json.dump(numbers, f_obj) #  json.dump() function to store the list numbers in the file numbers.json
    #  function takes two arguments: 
        # ---a piece of data to store 
        # --- a file object it can use to store the data
#print(numbers)
