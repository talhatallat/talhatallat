
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
# Even numbers are always divisible by two, so if the modulo of a number and two is zero (here, if number % 2 == 0) the number is even. Otherwise, it’s odd.
if number % 2 == 0:
  print("\nThe number " + str(number) + " is even.")
else:
  print("\nThe number " + str(number) + " is odd.")
