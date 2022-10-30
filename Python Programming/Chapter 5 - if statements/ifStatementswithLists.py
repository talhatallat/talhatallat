available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

# 5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:
# • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.

users = ['admin','eric', 'john', 'james', 'conor']
for user in users:
    if user == 'admin':
        print('Hello ' +user.title() +', would you like to see a status report?')
    else:
        print('Hello ' + user.title() + ', thank you for logging in again.')
    

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
#• If the list is empty, print the message We need to find some users!
#• Remove all of the usernames from your list, and make sure the correct message is printed.

users = []
if users:
    for user in users:
        if user == 'admin':
            print('\nHello ' +user.title() +', would you like to see a status report?')
        else:
            print('Hello ' + user.title() + ', thank you for logging in again.')

else:
    print('\nWe need to find some users!')

# 5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#• Make a list of five or more usernames called current_users.
#• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
#• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
#• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.

current_users = ['Admin','Eric', 'john', 'James', 'conor']
new_users = ['Conor','Admin','Amana', 'Ali', 'jamy']

current_users_lower = [user.lower() for user in current_users] # making list all lower cases 

for new_user in new_users:
    if new_user.lower() in  current_users_lower:
        print(f"\nSorry {new_user}, username is not available.")
    else:
        print('\nHi ' + new_user +', username is available.')

# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
#• Store the numbers 1 through 9 in a list.
#• Loop through the list.
#• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
numbers = [1,2,3,3,5,6,7,8,9] # = list(range(1,10))
for number in numbers:
    if number == 1:
        print("\n1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")


    

    
    
    
