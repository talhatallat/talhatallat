# the else block

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    
    try:
        answer = int(first_number) / int(second_number) #  the division operation in a try block
        
    except ZeroDivisionError: 
    #  which includes only the code that might cause an error. 
    # Any code that depends on the try block succeeding is added to the else block.
    # The except block tells Python how to respond when a ZeroDivisionError arises
        print("You can't divide by 0!")
    else:
        print(answer)
    
    # The try-except-else block works like this: Python attempts to run the code in the try statement. The only code that should go in a try statement is code that might cause an exception to be raised. 
    # Sometimes you’ll have additional code that should run only if the try block was successful; this code goes in the else block. The except block tells Python what to do in case a certain exception arises when it tries to run the code in the try statement.
