# Writing to an Empty File
filename = 'programming.txt'

with open(filename, 'w') as file_object: #  open() in this example has two arguments. 1st the name of the file we want to open. The 2nd argument, 'w', tells Python that we want to open the file in write mode.
  file_object.write("I love programming.\n") # write() method on the file object to write a string to the file.

# You can open a file in read mode ('r'), 
# write mode ('w'), append mode ('a'), 
# or a mode that allows you to read and write to the file ('r+'). 
# If you omit the mode argument, Python opens the file in read-only mode by default.


# Writing Multiple Lines
  file_object.write("I love creating new games.\n")

 
# Appending to a File

with open(filename, 'a') as file_object:#'a' argument to open the file for appending rather than writing over the existing file
   file_object.write("I also love finding meaning in large datasets.\n") #  write two new lines, which are added to programming.txt:
   file_object.write("I love creating apps that can run in a browser.\n")
