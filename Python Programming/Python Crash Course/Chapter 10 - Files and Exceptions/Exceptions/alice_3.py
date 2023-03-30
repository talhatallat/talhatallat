# I moved the file alice.txt to the correct directory, so the try block will work this time.  

filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()

except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # Count the approximate number of words in the file. we take the string contents, which now contains the entire text of Alice in Wonderland as one long string, and use the split() method to produce a list of all the words in the book.
    words = contents.split()
    # When we use len() on this list to examine its length, we get a good approximation of the number of words in the original string ➋. 
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
    # At ➌ we print a statement that reports how many words were found in the file. This code is placed in the else block because it will work only if the code in the try block was executed successfully. The output tells us how many words are in alice.txt:
# The file alice.txt has about 29461 words.
