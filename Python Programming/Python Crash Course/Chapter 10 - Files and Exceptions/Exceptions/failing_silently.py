# Failing Silently
# In the previous example, we informed our users that one of the files was unavailable. But you don’t need to report every exception you catch. 
# Sometimes you’ll want the program to fail silently when an exception occurs and continue on as if nothing happened. To make a program fail silently, you write a try block as usual, but you explicitly tell Python to do nothing in the except block. Python has a pass statement that tells it to do nothing in a block:

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
        #  Now when a FileNotFoundError is raised, the code in the except block runs, but nothing happens. No traceback is produced, and there’s no output in response to the error that was raised.
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
