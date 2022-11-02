# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102) by replacing your series of print statements with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.
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
    
#6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

rivers = {
    'nile': 'egypt', 
    'amazon': 'brazil', 
    'mekong': 'vietnam'
}

print("\n")
#Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for river,country in rivers.items():
    print("The " +river.title()+ " runs through " +country.title()+".")


#Use a loop to print the name of each river included in the dictionary.
print("\nRivers in data set:")
for river in rivers.keys():
    print(river.title())

#Use a loop to print the name of each country included in the dictionary.
print("\nCountries in data set:")
for country in rivers.values():
    print(country.title())
    
# 6-6. Polling: Use the code in favorite_languages.py (page 104).
favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
#• Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
coders = {'ali', 'jamal', 'sarah', 'jen', 'usman', 'philip'}
#• Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.
print("\n\n")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
print("\n")
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Thank you, {coder.title()} for responding!")
    else:
        print(f"{coder.title()} what is your favorite programming language?")

