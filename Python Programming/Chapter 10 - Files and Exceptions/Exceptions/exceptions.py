# 10-6. Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you’ll get a TypeError. 
#   Write a program that prompts for two numbers. Add them together and print the result. 
#   Catch the TypeError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.
try:
    user_input = input("Please enter a number: ")
    user_input2 = input("2nd number: ")
    cal = int(user_input) / int(user_input2)
except ValueError:
        print("numbers were not provided!")
else:
    print(cal)

# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    try:
        user_input = input("Please enter a number: ")
        user_input2 = input("2nd number: ")
        if (user_input and user_input2) == 'q':
            break
        cal = int(user_input) / int(user_input2)
    except ValueError:
            print("numbers were not provided!")
    else:
        print(cal)
        
# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. 
# Write a program that tries to read these files and print the contents of the file to the screen. 
# Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. 
# Move one of the files to a different location on your system, and make sure the code in the except block executes properly.


filenames = ['cats.txt', 'dogs.txt'] # two elements in a list stored as txt files 
for filename in filenames: # looping through the two txt files 
    print("\nfilename: "  + filename) # printing name of the files
    try:
        with open(filename) as f_obj: # opening files as an object 
            print(f_obj.read()) # printing the data read from an object

    except FileNotFoundError:
        print("Sorry! the file is missing.")

# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if either file is missing.
filenames = ['cats.txt', 'dogs.txt'] # two elements in a list stored as txt files in a variable
for filename in filenames: # looping through the two txt files 
    
    try:
        with open(filename) as f_obj: # opening files as an object 
            data = f_obj.read()

    except FileNotFoundError:
        pass

    else:
        print("\nReading file: " + filename)
        print(data)

# 10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/)
    
