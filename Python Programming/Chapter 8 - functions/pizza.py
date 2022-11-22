# Passing an Arbitrary Number of Arguments

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
