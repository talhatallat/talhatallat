# Find a Prime Number
def check_number (n):
    i = 2
    is_prime = True
    while i < n :
        if n % i == 0 :
            is_prime = False
            break # break once it divides 
        i = i + 1
    return is_prime

# ask user to input a number
n = int(input("Please enter any number"))
flag = check_number(n)
if  flag :
    print("Number is a prime.")
else:
    print("Number is not prime.")

# set a number
flag = check_number(100)
if  flag :
    print("Number is a prime.")
else:
    print("Number is not prime.")
