filename = 'pi_digits.txt' # reading a file from a directory where you’ll store this chapter’s programs.

with open(filename) as file_object: #  The open() function needs one argument: the name of the file you want to open.
  lines = file_object.readlines() #readlines() method takes each line from the file and stores it in a list.

pi_string = '' #  pi_string, to hold the digits of pi.
for line in lines: # a loop that adds each line of digits to pi_string
  #pi_string += line.rstrip() #  removes the newline character from each line
  pi_string += line.strip() #  get rid of whitespace that was on the left side of the digits in each line
  

print(pi_string[:52] + "...") #print this string only the first 50 decimal places
print(len(pi_string)) # show how long the string is
