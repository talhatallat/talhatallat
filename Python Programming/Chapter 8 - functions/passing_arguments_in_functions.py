# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.
def make_shirt(size, text):
    """Display information about a t shirt."""
    print("\nThe size of the shirt is "+ size.title() + " and the message printed on the shirt is " + text.title() +".")
#Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
make_shirt('large', 'superman')

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
def make_shirt(size='large', text='I love Python'):
    """Display information about a t shirt."""
    print("\nThe size of the shirt is "+ size.title() + " and the message printed on the shirt is " + text.title() +".")
make_shirt()
make_shirt('small')
make_shirt('medium', 'I love programming')

# 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.
def describe_city(city, country ='india'):
    """Display information about a t shirt."""
    print("\n" + city.title() + " is in " + country.title() +".")
describe_city('mumbai')
describe_city('new delhi')
describe_city('reykjavik', 'iceland')
