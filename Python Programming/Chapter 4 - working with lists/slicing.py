# 4-10-1. Slices: Using a slice to print the first three items from list.
slices = ['poo', 'loo', 'goo', 'koo', 'moo']
print("The first three items in the list are:")
for slice in slices[:]:
    print(slice.title())
    
# 4-10-2. Using a slice to print three items from the middle of the list.
print("\nThree items from the middle of the list are:")
for slice in slices[1:4]:
    print(slice.title())
    
# 4-10-3. Using a slice to print the last three items in the list.
print("\nThe last three items in the list are:")
for slice in slices[-3:]: #last three [-3:]
    print(slice.title())

print("\n")

# 4-11.1  Add a new pizza to the original list.
pizzas = ['margherita', 'veggie', 'pepperoni'] 
friend_pizzas = pizzas[:]

# 4-11.2 Add a new pizza to the original list.
pizzas.append('hawaiian')
# 4-11.3 Add a different pizza to the list friend_pizzas.
friend_pizzas.append('BBQ chicken pizza')

# Proving that you have two separate lists. Print the message, My favorite pizzas are:, and then use a for loop to print the first list. Print the message, My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

print("My favorite pizzas are: ")
print(pizzas)
 
print("\nMy friend's favorite pizzas are: ")
print(friend_pizzas)

print("\n")
# 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing to save space. Choose a version of foods.py, and write two for loops to print each list of foods.
for foods in pizzas[:]:
    #print(foods)
print("\n")
for friend_foods in friend_pizzas[:]:
    print(friend_foods)
