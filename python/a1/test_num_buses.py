import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """
    def test_one(self):
      """
        Test if we get correct value for corner case
      """  
      self.assertEqual(a1.num_buses(1), 1)

    def test_empty(self):
      """
        Test if exception is raised when we pass incorrect args
      """  
      self.assertRaises(ValueError, a1.num_buses, 0)

    def test_multi(self):
      """
        Test for some corner cases for more than 1 bus
      """  
      self.assertEqual(a1.num_buses(100), 2)      
      self.assertEqual(a1.num_buses(101), 3)

if __name__ == '__main__':
    unittest.main(exit=False)
