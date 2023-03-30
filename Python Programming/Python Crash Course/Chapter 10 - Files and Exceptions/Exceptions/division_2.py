#  try-except block for handling the ZeroDivisionError exception looks like:

#  the line that caused the error, inside a try block. If the code in a try block works, Python skips over the except block.
#  If the try block causes an error, Python looks for an except block whose error matches the one that was raised and runs the code in that block.
try:
    print(5/0) #  causes the error
except ZeroDivisionError:
    print("You can't divide by zero!")

# In this eg., the code in the try block produces a ZeroDivisionError, so Python looks for an except block telling it how to respond. 
# Python then runs the code in that block, and the user sees a friendly error message instead of a traceback: ZeroDivisionError: division by zero")
