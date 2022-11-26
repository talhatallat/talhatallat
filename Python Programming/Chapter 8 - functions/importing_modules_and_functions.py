# printing_models.py
def print_models(unprinted_designs, completed_models):
    # At ➊ we define the function print_models() with two parameters: a list of designs that need to be printed and a list of completed models. Given these two lists, the function simulates printing each design by emptying the list of unprinted designs and filling up the list of completed models.
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    #  At ➋ we define the function show_completed_models() with one parameter: the list of completed models. Given this list, show_completed_models() displays the name of each model that was printed.
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        

        
        
        
        
        
# print_models.py
# 8-15. Printing Models: Put the functions for the example print_models.py in a separate file called printing_functions.py. Write an import statement at the top of print_models.py, and modify the file to use the imported functions.
from printing_models import *

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)






# import_functions.py
# 8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
# import module_namefrom module_name 
# import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *
from print_models import *