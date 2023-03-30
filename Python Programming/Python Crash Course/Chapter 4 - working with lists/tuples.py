dimensions = (200, 50) # parentheses instead of square brackets.
print(dimensions[0]) #  print each element in the tuple individually, using the same syntax to access elements in a list.
print(dimensions[1]) 
# dimensions[0] = 250 # 'tuple' object does not support item assignment

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
    

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
foods = ('fish', 'yogurt', 'nuts', 'berries', 'lentils')
for food in foods[:]:
    print(food)

#foods[0] = 'h' # 'tuple' object does not support item assignment
print("\n")
foods = ('vegetables', 'apples', 'nuts', 'berries', 'lentils')
for food in foods[:]:
    print(food)
#print(foods)
