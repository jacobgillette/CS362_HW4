import unittest
import cat_name


class TestCase(unittest.TestCase):
  
  def test_vol0(self):
    #Tests a normal passing case
    self.assertEqual(cat_name.name("John", "Deere"), "John Deere")
  

  def test_vol1(self):
    #Tests incorrect order of first and last name (failing case)
    self.assertEqual(cat_name.name("Gillette", "Jacob"), "Jacob Gillette")

  def test_vol2(self):
    #manually inputted space to seperate first and last name (should cause fail)
    self.assertEqual(cat_name.name("Zoyla", " Badachi"), "Zoyla Badachi")

if __name__ == '__main__':
  unittest.main(verbosity=2)