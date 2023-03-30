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
# The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
# Move the show_privileges() method to this class. 
# Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its privileges.

class privileges():
    """Class with one attribute"""
    def __init__(self, privileges = ["can add post", "can delete post", "can ban user"]):
        self.privileges = privileges
    
    def show_privileges(self): # method 2
        for sets_of_privileges in self.privileges:
            print("'"+ sets_of_privileges.title() + 
            "' is one of privileges a administrator's have!!!")
    
class admin(privileges):
    """Admin class that inherits from the User class"""
    def __init__(self, privileges= ["can add post", "can delete post", "can ban user"]):# method 1 with a attribute stores list od strings
        # Make a Privileges instance as an attribute in the Admin class. 
        super().__init__(privileges)
    
        
my_admin = admin() # instances 1
my_admin.show_privileges() # calling a method to show its privileges.

# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method should check the battery size and set the capacity to 85 if it isn’t already. 
# Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. You should see an increase in the car’s range.

class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

#  we define a new class called Battery that doesn’t inherit from any other class.
class Battery():
    """A simple attempt to model a battery for an electric car."""
    # as one parameter, battery_size, in addition to self,   optional parameter sets the battery’s size to 70 if no value is provided
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    #  The method describe_battery() has been moved to this class as well
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    #  If the battery’s capacity is 70 kWh, get_range() sets the range to 240 miles, and if the capacity is 85 kWh, it sets the range to 270 miles. It then reports this value.
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    
    # Method checks the battery size and setting the capacity to 85 if it isn’t already. 
    def upgrade_battery(self):
        #print("Previous battery size: "+self.battery_size)
        self.battery_size = 85
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.Then initialize attributes specific to an electric car."""
        # The super() function at is a special function that helps Python make connections between the parent and child class. This line tells Python to call the __init__() method from ElectricCar’s parent class, which gives an ElectricCar instance all the attributes of its parent class. The name super comes from a convention of calling the parent class a superclass and the child class a subclass.
        super().__init__(make, model, year)
        #  This line tells Python to create a new instance of Battery
        self.battery = Battery()
    # Defining Attributes and Methods for the Child Class
        self.battery_size = 70
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    # Overriding Methods from the Parent Class
    def fill_gas_tank():
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

        
#  we make an instance of the ElectricCar class, and store it in my_tesla. This line calls the __init__() method defined in ElectricCar, which in turn tells Python to call the __init__() method defined in the parent class Car. We provide the arguments 'tesla', 'model s', and 2016.

# Make an electric car with a default battery size, 
    # call get_range() once, and then 
    # upgrading the battery, then 
    # call get_range() a second time, You should see an increase in the car’s range.

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
#my_tesla.describe_battery()
my_tesla.battery.describe_battery()
# The output tells us the range of the car based on its battery size
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
