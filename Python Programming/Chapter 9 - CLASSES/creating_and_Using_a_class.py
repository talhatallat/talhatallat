# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.

#Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
class restaurant():
    """ Making a class"""
    def __init__(self, restaurant_name, cuisine_type): # __init__() method has two attributes
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    
    def describe_restaurant(self): # method 2
        """  prints these two pieces of information """
        print("\n" + self.restaurant_name.title() +" restaurant serves " + self.cuisine_type.title() +" cuisine to customers.")
    
    def open_restaurant(self): # method 3
        """ Resturant is open. """
        print("\n"+ self.restaurant_name.title() +" restaurant is OPEN!\n")
        
my_restaurant = restaurant("Talhas" , 'indian') # instances 1
my_restaurant.describe_restaurant() #instances 2
my_restaurant.open_restaurant() # 3

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.
restaurant_1st = restaurant("jamis" , 'german')
restaurant_2nd = restaurant("pekoos" , 'caribbean')
restaurant_3rd = restaurant("tekos" , 'korean')

restaurant_1st.describe_restaurant()
restaurant_1st.open_restaurant() 

restaurant_2nd.describe_restaurant()
restaurant_2nd.open_restaurant() 

restaurant_3rd.describe_restaurant()
restaurant_3rd.open_restaurant() 


# 9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user.
#Create several instances representing different users, and call both methods for each user.
class users():
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    
    def describe_user(self):
        print("\n"+self.first_name.title() +" " +self.last_name.title() + " is " + self.age + " years old and lives in " + self.location.title()+".")
    
    def greet_user(self):
        print("Nice metting you " + self.first_name.title() +" " + self.last_name.title() + ", Have a good day.")

user_profile_1 = users('talha', 'tallat', '23', 'dublin')
user_profile_2 = users('usman', 'ghani', '26', 'pakistan')
user_profile_3 = users('mohsan', 'shreef', '21', 'dubai')

user_profile_1.describe_user()
user_profile_1.greet_user()

user_profile_2.describe_user()
user_profile_2.greet_user()

user_profile_3.describe_user()
user_profile_3.greet_user()
