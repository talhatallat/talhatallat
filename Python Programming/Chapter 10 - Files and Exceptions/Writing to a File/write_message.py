filename = 'programming.txt'

with open(filename, 'w') as file_object: #  open() in this example has two arguments. 1st the name of the file we want to open. The 2nd argument, 'w', tells Python that we want to open the file in write mode.
  file_object.write("I love programming.") # write() method on the file object to write a string to the file.

# You can open a file in read mode ('r'), 
# write mode ('w'), append mode ('a'), 
# or a mode that allows you to read and write to the file ('r+'). 
# If you omit the mode argument, Python opens the file in read-only mode by default.
