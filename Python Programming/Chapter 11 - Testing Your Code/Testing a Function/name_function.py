#  get_formatted_name() function combines the first and last name with a space in between to complete a full name, and then capitalizes and returns the full name
def get_formatted_name(first, last):   
  """Generate a neatly formatted full name."""    
  full_name = first + ' ' + last    
  return full_name.title()
