# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166). Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business.

class restaurant():
    """ Making a class"""
    def __init__(self, restaurant_name, cuisine_type): # __init__() method has two attributes
        self.restaurant_name = restaurant_name # 1 attributes
        self.cuisine_type = cuisine_type # 2 attributes
        self.number_served = 0
        
    
    def describe_restaurant(self): # method 2
        """  prints these two pieces of information """
        print("\n" + self.restaurant_name.title() +" restaurant serves " + self.cuisine_type.title() +" cuisine to customers.")
    
    def open_restaurant(self): # method 3
        """ Resturant is open. """
        print("\n"+ self.restaurant_name.title() +" restaurant is OPEN!\n")
    
    def read_number_served(self): # method 4
        """Print a statement showing the numbers served"""
        print("The restaurant has only served " + str(self.number_served) + " customers.")
    
    def set_number_served(self, served):
        self.number_served = served
    
    def increment_number_served(self, served):
        self.number_served += served
            
        
        
my_restaurant = restaurant("Talhas" , 'indian') # instances
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(123)
my_restaurant.read_number_served()

my_restaurant.increment_number_served(123)
my_restaurant.read_number_served()

print("\n\n\n")
# 9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166). Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
class users():
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        print("\n"+self.first_name.title() +" " +self.last_name.title() + " is " + self.age + " years old and lives in " + self.location.title()+".")
    
    def greet_user(self):
        print("Nice metting you " + self.first_name.title() +" " + self.last_name.title() + ", Have a good day.")
    
    def read_login_attempts(self): # method 4
        """Print a statement showing the numbers served"""
        print("Number of login attempets: " + str(self.login_attempts) + "")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user_profile_1 = users('talha', 'tallat', '23', 'dublin')
user_profile_2 = users('usman', 'ghani', '26', 'pakistan')
user_profile_3 = users('mohsan', 'shreef', '21', 'dubai')

user_profile_1.describe_user()
user_profile_1.greet_user()

user_profile_1.increment_login_attempts() # calling increment_login_attempts which increments the value of login_attempts to 1
user_profile_1.increment_login_attempts() # increment to 1
user_profile_1.increment_login_attempts() # increment to 1
user_profile_1.read_login_attempts() # displayes login_attempts

user_profile_1.reset_login_attempts() # reset to 0
user_profile_1.read_login_attempts() # displayes login_attempts

user_profile_2.describe_user()
user_profile_2.greet_user()

user_profile_3.describe_user()
user_profile_3.greet_user()



