# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = [
    'chicken sandwich',
    'pastrami sandwich', 
    'egg sandwich', 
    'tuna Sandwich', 
    'roast beef sandwich',
    'pastrami sandwich',
    'grilled sandwich',
    'ham sandwich',
    'nutella sandwich',
    'pastrami sandwich',
    'grilled chicken sandwich'
    ]

finished_sandwiches = []

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

print("Deli has run out of pastrami sandwich.\n")

while sandwich_orders:
    while 'pastrami sandwich' in  sandwich_orders:
        sandwich_orders.remove('pastrami sandwich')
    sandwich_order = sandwich_orders.pop()
    print("I made your " + (sandwich_order))
    
    
    finished_sandwiches.append(sandwich_order)
for finished_sandwich in finished_sandwiches:
    print("\n" + finished_sandwich.title() + " was made.")

print("\n\n")

# 7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.
dream_vacation = {}

polling_active = True

while polling_active:
    user = input("Please input your name: ")
    vacation = input("If you could visit one place in the world, where would you go: ")
    # Store the response of the user in the dictionary:
    dream_vacation[user] = vacation
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# print the results of the poll
for user,vacation in dream_vacation.items():
    print(user.title() + "'s dream vaction is "+ vacation.title() + ".")




    
