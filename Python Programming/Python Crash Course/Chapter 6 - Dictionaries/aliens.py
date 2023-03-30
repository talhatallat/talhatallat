# Make an empty list for storing aliens.   
aliens = []
# Make 30 green aliens.➊ 
for alien_number in range(30):
    new_alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens:➍ 
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.➎ 
print("Total number of aliens: " + str(len(aliens)))
