def get_formatted_name(first, middle, last):
  """Generate a neatly formatted full name."""
  full_name = first + ' ' + middle + ' ' + last
  return full_name.title()


# This version should work for people with middle names, but when we test it, we see that we’ve broken the function for people with just a first and last name. 
# This time, running the file test_name_function.py gives this output:
#---------------------------------------------------------------------------------------------
#➊ E   
# ======================================================================
#➋ ERROR: test_first_last_name (__main__.NamesTestCase)
# ----------------------------------------------------------------------
#➌ Traceback (most recent call last):     
#     File "test_name_function.py", line 8, in test_first_last_name
#     formatted_name = get_formatted_name('janis', 'joplin')
#   TypeError: get_formatted_name() missing 1 required positional argument: 'last'
# ----------------------------------------------------------------------
#➍ Ran 1 test in 0.000s
#➎ FAILED (errors=1)
#---------------------------------------------------------------------------------------------

#  E ➊, which tells us one unit test in the test case resulted in an error.
#  test_first_last_name() in NamesTestCase caused an error ➋.
#  ➌ we see a standard traceback, which reports that the function call get_formatted_name('janis', 'joplin') no longer works because it’s missing a required positional argument.
#  one unit test was run ➍.
#  overall test case failed and that one error occurred when running the test case ➎
