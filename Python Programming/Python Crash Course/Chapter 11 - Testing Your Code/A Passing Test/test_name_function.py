import unittest #  module unittest from the Python standard library provides tools for testing your code.
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase): # class will contain a series of unit tests for get_formatted_name().  You can name the class anything you want
  """Tests for 'name_function.py'."""
  
  def test_first_last_name(self):
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin') #  we call get_formatted_name() with the arguments 'janis' and 'joplin', and store the result in formatted_name
    self.assertEqual(formatted_name, 'Janis Joplin') # unittest’s most useful features: an assert method. Assert methods verify that a result you received matches the result you expected to receive
    
unittest.main()
