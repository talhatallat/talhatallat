filename = 'pi_digits.txt'

# The keyword with closes the file once access to it is no longer needed. Notice how we call open() in this program but not close(). You could open and close the file by calling open() and close(), but if a bug in your program prevents the close() statement from being executed, the file may never close. This may seem trivial, but improperly closed files can cause data to be lost or corrupted. And if you call close() too early in your program, you’ll find yourself trying to work with a closed file (a file you can’t access), which leads to more errors. It’s not always easy to know exactly when you should close a file, but with the structure shown here, Python will figure that out for you. All you have to do is open the file and work with it as desired, trusting that Python will close it automatically when the time is right.
with open(filename) as file_object: #  The open() function needs one argument: the name of the file you want to open.
  for line in file_object:
    print(line.rstrip()) #  rstrip() eliminates these extra blank lines

