# Handling the ZeroDivisionError Exception
print(5/0) # Of course Python can’t do this, so we get a traceback:  ZeroDivisionError: division by zero
#  ZeroDivisionError, is an exception object.
#  Python creates this kind of object in response to a situation where it can’t do what we ask it to.
# When this happens, Python stops the program and tells us the kind of exception that was raised.

# We can use this information to modify our program. We’ll tell Python what to do when this kind of exception occurs; that way, if it happens again, we’re prepared.
