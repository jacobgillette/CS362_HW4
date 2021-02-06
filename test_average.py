import unittest
import average


class TestCase(unittest.TestCase):
  
  def test_vol0(self):
    #Tests input being equal to zero
    self.assertEqual(average.avg([99,0, 0]), 33)
  
  def test_vol1(self):
    #Tests a normal passing case
    self.assertEqual(average.avg([3,3,6]), 4)

  def test_vol2(self):
    #Tests an empty matrix which causes a failing case due to division by zero
    self.assertEqual(average.avg([]), 0)
    

if __name__ == '__main__':
  unittest.main(verbosity=2)