# 7-1. Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”
rental_car = input("What kind of rental car would you like? \nAnswer: ")
print("Let me see if I can find you a " + rental_car + ".")

# 7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
restaurant_seating = input("\nHow many people are there in your dinner group? \nAnswer: ")
restaurant_seating = int(restaurant_seating)
if restaurant_seating > 8:
    print("Sorry guys! you have to wait for a table.")
else:
    print("Your table is ready.")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.
multiples_of_ten = input("\nPlease enter a number? \nAnswer: ")
multiples_of_ten = int(multiples_of_ten)
if multiples_of_ten % 10 == 0:
    print("\n" +str(multiples_of_ten) + " is a multiple of 10")
else:
    print("\n" +str(multiples_of_ten) + " is a not multiple of 10")
