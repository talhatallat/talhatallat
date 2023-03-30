# 10-1. Learning Python: Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far. 
# Start each line with the phrase In Python you can.... Save the file as learning_python.
# txt in the same directory as your exercises from this chapter. 
# Write a program that reads the file and prints what you wrote three times. 
# Print the contents once by reading in the entire file, 
#   once by looping over the file object, 
#   and once by storing the lines in a list and then working with them outside the with block.

filename = 'learning_python.txt'

print("--- Reading in the entire file:")
with open(filename) as file_object:
    lines = file_object.read() # Print the contents once by reading in the entire file, 
    print(lines) # prints what you wrote three times

print("\n--- Looping over the lines:")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip()) 

print("\n--- Storing the lines in a list:")
with open(filename) as file_object:
    lines = file_object.readlines() #readlines() method takes each line from the file and stores it in a list.

for line in lines:
    print(line.rstrip()) #rstrip() eliminates these extra blank lines

# 10-2. Learning C: You can use the replace() method to replace any word in a string with a different word. Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence:
# >>> message = "I really like dogs.">>> message.replace('dog', 'cat')'I really like cats.'
#Read in each line from the file you just created, learning_python.txt, and replace the word Python with the name of another language, such as C. Print each modified line to the screen.
print("\n--- replace any word in a string with a different word: ")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.rstrip()
    replace= line.replace('Python','C') # replace() method to replace any word in a string with a different word
    print(replace) #rstrip() eliminates these extra blank lines



