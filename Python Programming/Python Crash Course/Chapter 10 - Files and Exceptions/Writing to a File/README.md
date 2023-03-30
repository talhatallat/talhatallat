You can open a file in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows you to read and write to the file ('r+').

#### example:
         filename = 'programming.txt'
         with open(filename, 'w') as file_object:
              file_object.write("I love programming.")
