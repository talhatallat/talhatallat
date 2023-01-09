# This program prompts the user to input a first_number ➊ and, if the user does not enter q to quit, a second_number ➋. 
# We then divide these two numbers to get an answer ➌. 
# This program does nothing to handle errors, so asking it to divide by zero causes it to crash:
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    
    answer = int(first_number) / int(second_number)
    print(answer)
