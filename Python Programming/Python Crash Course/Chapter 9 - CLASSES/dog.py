# Creating the Dog Class

class Dog():# 1
    """A simple attempt to model a dog."""#2
    
    #  Python will call the __init__() method from the Dog class. We’ll pass Dog() a name and an age as arguments; self is passed automatically, so we don’t need to pass it.
    def __init__(self, name, age):#3 A function that’s part of a class is a method.  Have three parameters
        """Initialize name and age attributes."""
        self.name = name #4  each have the prefix self,  Any variable prefixed with self is available to every method in the class.
        self.age = age #  Variables that are accessible through instances like this are called attributes.
        
    def sit(self): #5
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
        
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
