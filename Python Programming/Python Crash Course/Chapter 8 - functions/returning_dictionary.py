# 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
#"Santiago, Chile"
#Call your function with at least three city-country pairs, and print the value that’s returned.
def city_country(city, country):
    full_name = {'city': city, 'country': country}
    return full_name

m = city_country('santiago','chile')
print(m)
m = city_country('d','f')
print(m)
m = city_country('sf','fgsr')
print(m)


# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.
def make_album(artist, album, tracks=0):
    album = {'artist': artist, 'album': album}
# Add an optional parameter to make_album() that allows you to store the number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new function call that includes the number of tracks on an album.
    if album:
        album['tracks'] = tracks
    return album
a = make_album('s','c', 2)
print(a)
a = make_album('s','c', 3)
print(a)
a = make_album('s','c', 4)
print(a)
# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.
while True:   
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    artist = input("Who's the artist?")
    if artist == 'q':
        break
    album = input("What album are you thinking of? ")
    if album == 'q':
        break
 
    a = make_album(artist, album)
    print(a)
print("\nThanks for responding!")
