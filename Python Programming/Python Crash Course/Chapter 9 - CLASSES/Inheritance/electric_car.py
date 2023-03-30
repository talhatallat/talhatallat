# Inheritance

# When you create a child class, the parent class must be part of the current file and must appear before the child class in the file.

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
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.battery.describe_battery()
# The output tells us the range of the car based on its battery size
my_tesla.battery.get_range()
