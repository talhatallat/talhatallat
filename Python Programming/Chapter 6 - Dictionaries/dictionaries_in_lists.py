# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.
people = {
    'pkolo':{
        'first_name': 'penokeo',
        'last_name': 'kolo',
        'age': 31, 
        'city': 'lisbon'
    },
    'jkennedy':{
        'first_name': 'john',
        'last_name': 'kennedy',
        'age': 26, 
        'city': 'london'
    },
    'pkitoo':{
        'first_name': 'paul',
        'last_name': 'kitoo',
        'age': 29, 
        'city': 'new york'
    },
}

for username, user_info in people.items():
    print("\nUsername: " + username)
    full_name = user_info['first_name'] + " " + user_info['last_name']
    location = user_info['city']
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do print everything you know about each pet.
pets = {
    'charlie':{
        'animal': 'dog',
        'owners_name': 'kolo',
    },
    'maxi':{
        'animal': 'cat',
        'owners_name': 'john',
    },
    'buddy':{
        'animal': 'snake',
        'owners_name': 'paul',
    },
}

for pet, user_info in pets.items():
    print("\nName of the Pet: " + pet)
    name = user_info['animal']
    o_name = user_info['owners_name']
    
    print("\tAnimal: " + name.title())
    print("\tOwner's name: " + o_name.title())
    
# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.
favorite_places = {
    'john': ['vienna', 'paris', 'bern',],
    'paul': ['warsaw', 'bucharest', 'valletta',],
    'jamal': ['zagreb', 'sofia', 'stockholm',]
}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are: ")
    for place in places:
        print("-> "+ place.title())

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

favorite_numbers = {
    'ali': [1,2,3], 
    'jamal': [4,5,6], 
    'doa': [7,8,9], 
    'khalid': [10,11,12], 
    'hanna': [13,14,15]
}

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are: ")
    for number in numbers:
        print("-> " + str(number).title())

# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    'stockholm': {
        'country': 'sweeden',
        'population': '975,551 (Dec 31, 2020)',
        'fact': "Stockholm is built on 14 islands and cleanest cities in Europe."
    },
    'bucharest': {
        'country': 'romania',
        'population': '1.83 million (2019)',
        'fact': "Bucharest is also called Little Paris. The city's Arcul de Triumf was constructed in 1935 to be modeled after the Arc de Triomphe in Paris."
    },
    'sofia': {
        'country': 'bulgaria',
        'population': '1.236 million (2017)',
        'fact': "Sofia is one of the oldest capital cities in Europe and it is in the west of Bulgaria"
    }
}

for city, other_info in cities.items():
    print("\n" + city.title() + 
        " is a capital of " + other_info['country'].title() + 
        " and has a population of " + other_info['population'] + 
        " and " + other_info['fact'])
