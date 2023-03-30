seeing_the_world = ['los vagus', 'new york', 'swizerland', 'malta', 'punjab'] # 3-8-1

print("Orginal list of places i want to goto: ")
print(seeing_the_world) # 3-8-2

print("\nSorting list in alphabetical Order: ") 
print(sorted(seeing_the_world))# 3-8-3

print("\nSorting list in reverce alphabetical Order: ") 
print(sorted(seeing_the_world, reverse = True))# 3-8-5
#print(seeing_the_world)

print("\nOriginal list of places again: ")
print(seeing_the_world)# 3-8-6

print("\nlist order is reversed: ") # 3-8-7
seeing_the_world.reverse() 
print(seeing_the_world)

print("\nlist order has changed again: ") # 3-8-8
seeing_the_world.reverse() 
print(seeing_the_world)

print("\nList in Alphabetical order:") # 3-8-9
seeing_the_world.sort()
print(seeing_the_world)

print("\nList in reverce Alphabetical order:") # 3-8-10
seeing_the_world.sort(reverse=True)
print(seeing_the_world)



cities = ['dublin', 'cork', 'sligo', 'galway', 'roscommon'] # 3-10
#cities.title()
print(cities[0].title())

cities = ['waterford', 'wexford', 'belfast']
print(cities[0].title())

cities.append('donegal') #  adds 'donegal' to the end of the list
cities.insert(1, 'carlow') #Inserting Element at index 1 into a List
del cities[0]# Removing an Item Using the del Statement at index 0
cities.pop()# Removing an Item Using the pop() Method
cities.pop(1)#Popping Items from any Position in a List
print(cities)

