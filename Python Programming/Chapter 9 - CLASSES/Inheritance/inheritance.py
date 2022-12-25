# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
#   Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). 
#   Either version of the class will work; just pick the one you like better. 
        # Add an attribute called flavors that stores a list of ice cream flavors. 
        # Write a method that displays these flavors. 
        # Create an instance of IceCreamStand, and call this method.

class restaurant():
    """Making a class"""
    def __init__(self, restaurant_name, cuisine_type): # __init__() method has two attributes
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    
    def describe_restaurant(self): # method 2
        """  prints these two pieces of information """
        print("\n" + self.restaurant_name.title() +" restaurant serves " + self.cuisine_type.title() +" cuisine to customers.")
    
    def open_restaurant(self): # method 3
        """ Resturant is open. """
        print("\n"+ self.restaurant_name.title() +" restaurant is OPEN!\n")
        
        
class icecream_stand(restaurant): # class IceCreamStand inherits from the Restaurant class
    """A simple attempt to represent a car."""
    def __init__(self, flavors = ["vanilla", "choclate", "strawberry", "cookies & cream"]):
        self.flavors = flavors
        
        
    def display_flavors(self): # method 1
        """ Resturant is open. """
        for list_of_flavors in self.flavors:
            print(list_of_flavors.title() +" is a great Ice cream flavor.")
        


my_icecream_stand = icecream_stand() # instances 1
my_icecream_stand.display_flavors() # # calling a method

print("\n")
# 9-7. Admin: An administrator is a special kind of user. 
# Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) or Exercise 9-5 (page 171). 
# Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. 
# Write a method called show_privileges() that lists the administrator’s set of privileges.
# Create an instance of Admin, and call your method.

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


class admin(users):
    """Admin class that inherits from the User class"""
    def __init__(self, privileges= ["can add post", "can delete post", "can ban user"]):# method 1 with a attribute init 
        self.privileges = privileges
    
    def show_privileges(self): # method 2
        for sets_of_privileges in self.privileges:
            print("'"+ sets_of_privileges.title() + 
            "' is one of privileges a administrator’s have!")
        
my_admin = admin() # instances 2
my_admin.show_privileges() # calling a method

# 9-8. Privileges: Write a separate Privileges class. 
#The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
# Move the show_privileges() method to this class. 
# Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its privileges.
