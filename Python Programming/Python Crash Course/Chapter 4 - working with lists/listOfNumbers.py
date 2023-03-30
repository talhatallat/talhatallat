# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for ct in range(1,21):
    print(ct)

# 4-3.1 list of numbers using comprehension method 
lon = [value+1 for value in range(0,21)]
print(lon)

# 4-4 + 4-5. Summing a Million: Made a list of the numbers from one to one million, and then use min() and max() to start list at one and ends at one million. and using sum() function.
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#  4-6 Used the third argument of the range() function to make a list of the odd numbers from 1 to 20
oddNumbers = [value+1 for value in range(0,21,2)] # [for loop with range of numbers and adds 2] to produce odd numbers 
print(oddNumbers)

#  4-7 Make a list of the multiples of 3 from 3 to 30.
threes = [value+0 for value in range(3,30,3)]
print(threes)

# 4-8 made a list of the first 10 cubes (that is, the cube of each integer from 1 through 10)
listCubes = []
for value in range(1,11):
    cube = value**3 # value^3
    listCubes.append(cube)
    print(listCubes, "\n")

# 4-9. Used a list comprehension to generate a list of the first 10 cubes
cubeComprehension = [value**3 for value in range(1,11)]
print(cubeComprehension)
