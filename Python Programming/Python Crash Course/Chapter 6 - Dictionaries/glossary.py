# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

person = {'first_name': 'penokeo', 'last_name': 'kolo', 'age': 24, 'city': 'new york'}


# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

favorite_numbers = {'ali': 2, 'jamal': 5, 'doa': 8, 'khalid': 7, 'hanna': 1}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

num = favorite_numbers['ali']
print(f"\nAli's favorite number is {num}.")

num = favorite_numbers['jamal']
print(f"Jamal's favorite number is {num}.")

num = favorite_numbers['doa']
print(f"Doa's favorite number is {num}.")

num = favorite_numbers['khalid']
print(f"Khalid's favorite number is {num}.")

num = favorite_numbers['hanna']
print(f"Hanna's favorite number is {num}.")

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }
#• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
word = 'string'
print("\nWhat is "+word+"?\n" + glossary['string'])
word = 'comment'
print("\nWhat is "+word+"?\n" + glossary['comment'])
word = 'list'
print("\nWhat is "+word+"?\n" + glossary['list'])
word = 'loop'
print("\nWhat is "+word+"?\n" + glossary['loop'])
word = 'dictionary'
print("\nWhat is "+word+"?\n" + glossary['dictionary'])
