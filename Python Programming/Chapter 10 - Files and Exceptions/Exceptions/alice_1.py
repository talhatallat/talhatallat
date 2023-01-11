# Python can’t read from a missing file, so it raises an exception:
#-------------------------------------------
# Traceback (most recent call last):  
# File "alice.py", line 3, in <module>    
# with open(filename) as f_obj:
# FileNotFoundError: [Errno 2] No such file or 
# directory: 'alice.txt'
#--------------------------------------------
filename = 'alice.txt'

with open(filename) as f_obj:
    contents = f_obj.read()
# The last line of the traceback reports a FileNotFoundError: this is the exception Python creates when it can’t find the file it’s trying to open.
