# 9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you used a standard dictionary to represent a glossary. 
# Rewrite the program using the OrderedDict class and make sure the order of the output matches the order in which key-value pairs were added to the dictionary.
from collections import OrderedDict

glossary = OrderedDict()
# Dictionaries allow you to connect pieces of information, but they don’t keep track of the order in which you add key-value pairs. If you’re creating a dictionary and want to keep track of the order in which key-value pairs are added, you can use the OrderedDict class from the collections module. Instances of the OrderedDict class behave almost exactly like dictionaries except they keep track of the order in which key-value pairs are added.

python_terms  = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
}
    
python_terms['key'] = 'The first item in a key-value pair in a dictionary.'
python_terms['value'] = 'An item associated with a key in a dictionary.'
python_terms['conditional test'] = 'A comparison between two values.'
python_terms['float'] = 'A numerical value with a decimal component.'

for keys,values in python_terms.items():
    #print("Programming word " +keys +", means: " + values)
    print(f"{keys.title()}: {values}")

# 9-14. Dice: The module random contains functions that generate random numbers in a variety of ways. The function randint() returns an integer in the range you provide. 
# The following code returns a number between 1 and 6: 
# from random import randint
# x = randint(1, 6)

# Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides
        
    def roll_die(self):
        x = randint(1, self.sides)
        return x
        

d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

d10 = Die(sides =10)
for sides10 in range(10):
    result = d10.roll_die()
    results.append(result)
print("10 rolls of a 10-sided die:")
print(results)

d20 = Die(sides =20)
for sides10 in range(10):
    result = d20.roll_die()
    results.append(result)
print("10 rolls of a 20-sided die:")
print(results)

# 9-15. Python Module of the Week: One excellent resource for exploring the Python standard library is a site called Python Module of the Week. 
# Go to http://pymotw.com/ and look at the table of contents. Find a module that looks interesting to you and read about it, or explore the documentation of the collections and random modules.
