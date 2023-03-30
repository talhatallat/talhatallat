

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

# Now we can write a simple loop to count the words in any text we want to analyze. We do this by storing the names of the files we want to analyze in a list, and then we call count_words() for each file in the list. We’ll try to count the words for Alice in Wonderland, Siddhartha, Moby Dick, and Little Women, which are all available in the public domain. I’ve intentionally left siddhartha.txt out of the directory containing word_count.py, so we can see how well our program handles a missing file:
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
    
# The missing siddhartha.txt file has no effect on the rest of the program’s execution
# Using the try-except block in this example provides two significant advantages. We prevent our users from seeing a traceback, and we let the program continue analyzing the texts it’s able to find. If we don’t catch the FileNotFoundError that siddhartha.txt raised, the user would see a full traceback, and the program would stop running after trying to analyze Siddhartha. It would never analyze Moby Dick or Little Women.
