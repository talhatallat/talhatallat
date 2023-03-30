# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
alien_color = 'green'
#  if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
if alien_color == 'green':
    points = 5
    print("Player just earned", (points),"points.")
#  one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
elif alien_color == 'yellow':
    points = 0
    print("Player just earned", (points),"points.")
#else:
  #  print("Player has no output.")
    
# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
alien_color = 'red'
#  If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
if alien_color == 'green':
    points = 5
    print("Player just earned", (points),"points.")
# If the alien’s color isn’t green, print a statement that the player just earned 10 points.
if alien_color != 'green':
    points = 10
    print("Player just earned", (points),"points.")
#  Write one version of this program that runs the if block and another that runs the else block.
else:
    points = 0
    print("Player just earned", (points),"points.")
    
#  Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
#• If the alien is green, print a message that the player earned 5 points.
#• If the alien is yellow, print a message that the player earned 10 points.
#• If the alien is red, print a message that the player earned 15 points.
#• Write three versions of this program, making sure each message is printed for the appropriate color alien.

alien_color = 'yellow'
if alien_color == 'green':
    points = 5
    print("Player just earned", (points),"points.")
elif alien_color == 'yellow':
    points = 10
    print("Player just earned", (points),"points.")
elif alien_color == 'red':
    points = 15
    print("Player just earned", (points),"points.")

# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
#• If the person is less than 2 years old, print a message that the person is a baby.
#• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
#  If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# • If the person is age 65 or older, print a message that the person is an elder.

age = 20
if age < 2:
    print("The person is baby.")
elif age <4:
    print("Person is a toddler.")
elif age<13:
    print("Person is a teenager.")
elif age >=20 and age < 65:
    print("Person is an adult.")
else:
    print("Person is an  elder.")


# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
#• Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!

favorite_fruits = ['apple', 'banana', 'blueberry', 'orange', 'straberry']
if 'banana' in  favorite_fruits:
    print("You really like bananas!")
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'orange' in favorite_fruits:
    print("You really like oranges!")
if 'blueberry' in favorite_fruits:
    print("You really like blueberries!")
if 'straberry' in favorite_fruits:
    print("You really like straberrys!")
