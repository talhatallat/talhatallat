# <a href="https://github.com/talhatallat/talhatallat/blob/main/Python%20Programming/Chapter%208%20-%20functions/functions.py">functioncs.py<a/>
* Defining a Function
* Passing Information to a Function

## 8-1. Message: 
Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.
## 8-2. Favorite Book: 
Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.

# <a href="https://github.com/talhatallat/talhatallat/blob/main/Python%20Programming/Chapter%208%20-%20functions/passing_arguments_in_functions.py">passing_arguments_in_functions.py</a>
* Positional Arguments
* Multiple Function Calls 
* Keyword Arguments
* Default Values
* Equivalent Function Calls


## 8-3. T-Shirt: 
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
## 8-4. Large Shirts: 
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
## 8-5. Cities: 
Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

# <a href="https://github.com/talhatallat/talhatallat/tree/main/Python%20Programming/Chapter%208%20-%20functions">returning_dictionary.py</a>
* Return Values
* Returning a Dictionary
* Using a Function with a while Loop
## 8-6. City Names: 
Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value that’s returned.
## 8-7. Album: 
Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.

Add an optional parameter to make_album() that allows you to store the number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new function call that includes the number of tracks on an album.
## 8-8. User Albums: 
Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.

# <a href="https://github.com/talhatallat/talhatallat/blob/main/Python%20Programming/Chapter%208%20-%20functions/modifying_a_List_in_a_Function.py">modifying_a_List_in_a_Function.py</a>
* Passing a List
* Modifying a List in a Function
* Preventing a Function from Modifying a List
## 8-9. Magicians: 
  Make a list of magician’s names. Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
## 8-10. Great Magicians: 
  Start with a copy of your program from Exercise 8-9. Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to see that the list has actually been modified.
## 8-11. Unchanged Magicians: 
  Start with your work from Exercise 8-10. Call the function make_great() with a copy of the list of magicians’ names. Because the original list will be unchanged, return the new list and store it in a separate list. Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name.

# <a href="https://github.com/talhatallat/talhatallat/blob/main/Python%20Programming/Chapter%208%20-%20functions/Passing_an_Arbitrary_Number_of_Arguments.py">Passing_an_Arbitrary_Number_of_Arguments.py<a/>
* Passing an Arbitrary Number of Arguments
* Mixing Positional and Arbitrary Arguments
* Using Arbitrary Keyword Arguments
## 8-12. Sandwiches: 
Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time.
## 8-13. User Profile: 
Start with a copy of user_profile.py from page 153. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.
## 8-14. Cars: 
Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:

car = make_car('subaru', 'outback', color='blue', tow_package=True)

Print the dictionary that’s returned to make sure all the information was stored
