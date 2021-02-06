import unittest
import cube_vol


class TestCase(unittest.TestCase):
  
  def test_vol0(self):
    #This case tests a negative input
    self.assertEqual(cube_vol.vol(1,1,-1), -1)

  def test_vol1(self):
    #Tests a input equal to zero
    self.assertEqual(cube_vol.vol(2,0, 1), 0)

  def test_vol2(self):
    #Tests a normal case
    self.assertEqual(cube_vol.vol(3,1,2), 6)

  def test_vol3(self):
    #Tests a failing case with an incorrect output
    self.assertEqual(cube_vol.vol(100,1,2), 201)

if __name__ == '__main__':
  unittest.main(verbosity=2)