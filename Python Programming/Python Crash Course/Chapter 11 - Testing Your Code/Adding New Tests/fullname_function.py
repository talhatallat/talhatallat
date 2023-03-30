import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
  """Tests for 'name_function.py'."""
  def test_first_last_name(self):
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    self.assertEqual(formatted_name, 'Janis Joplin')
    
  def test_first_last_middle_name(self):
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')  #call get_formatted_name() with a first, last, and middle name
    self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart') #  use assertEqual() to check that the returned full name matches the full name (first, middle, and last) that we expect

unittest.main()
