# 8-12.vr 1
def sandwiches(toppings):
    """Make a sandwich with the items a person wants."""
    loop = True
    while loop:
        user_toppings = input("\n\nI can make you a great sandwich: \nPress 'q' when you are finshed.\nToppings: ")
        
        if user_toppings == 'q':
            break
            loop = False
        print("Adding " + user_toppings.title() + " to your Sandwich.")
        
        toppings.append(user_toppings)
        
    for topping in toppings:
        print("\n"+topping.title() + " added to your sandwitch.")
    print("\nYour sandwich is ready!")
    
toppings = []
sandwiches(toppings)
sandwiches(toppings)
sandwiches(toppings)
        
# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time.
def make_sandwich(*items):
    #  but this (*items) parameter collects as many arguments as the calling line
    """Make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print("  ...adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')

# 8-13. User Profile: Start with a copy of user_profile.py from page 153. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.
def build_profile(first, last, **user_info):
    #  The double asterisks before the parameter **user_info cause Python to create an empty dictionary called user_info and pack whatever name-value pairs it receives into this dictionary. Within the function, you can access the name-value pairs in user_info just as you would for any dictionary.
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
    
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
my_profile = build_profile('talha', 'tallat', location='dublin', field='engineering')
print(user_profile)
print(my_profile)


# 8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:
#car = make_car('subaru', 'outback', color='blue', tow_package=True)
#Print the dictionary that’s returned to make sure all the information was stored correctly.

def make_car(manufacturer, model, **other_info):
    """Build a dictionary containing everything we know about a user."""
    cars_profile = {}
    cars_profile['manufacturer'] = manufacturer
    cars_profile['model name'] = model
    for key, value in other_info.items():
        cars_profile[key] = value
    return cars_profile
    
car1 = make_car('bmw', 'i8', colour='blue', owner='talha')
car2 = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car1)
print(car2)
