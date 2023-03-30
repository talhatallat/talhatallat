#  In this example, the open() function produces the error, so to handle it, the try block will begin just before the line that contains open():
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

#  the code in the try block produces a FileNotFoundError, so Python looks for an except block that matches that error.
#  Python then runs the code in that block, and the result is a friendly error message instead of a traceback:
# Sorry, the file alice.txt does not exist.
