
def get_formatted_name(first, last, middle=''):
  """Generate a neatly formatted full name."""
  
  if middle:
    full_name = first + ' ' + middle + ' ' + last
  else:
      full_name = first + ' ' + last
  return full_name.title()

# In this new version of get_formatted_name(), the middle name is optional. If a middle name is passed to the function (if middle:), the full name will contain a first, middle, and last name. Otherwise, the full name will consist of just a first and last name. Now the function should work for  both kinds of names. To find out if the function still works for names like Janis Joplin, let’s run test_name_function.py again:
# Ran 1 test in 0.000s
# OK
