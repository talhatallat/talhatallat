# the car class
class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year): # method has 3 parameters
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Setting a Default Value for an Attribute
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading: #  If the new mileage, mileage, is greater than or equal to the existing mileage, self.odometer_reading, you can update the odometer reading to the new mileage
            self.odometer_reading = mileage
        else:
            #  If the new mileage is less than the existing mileage, you’ll get a warning that you can’t roll back an odometer
            print("You can't roll back an odometer!")
        
    def increment_odometer(self, miles): # The new method increment_odometer() takes in a number of miles, and adds this value to self.odometer_reading.
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
