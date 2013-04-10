import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    
    def test_one(self):
      """
	Test list with only one element
      """
      L = [1]
      a1.swap_k(L, 1)
      self.assertEquals(L[0],1)
      

    def test_empty(self):
      """
        Test empty list
      """
      L = []
      a1.swap_k(L, 0)
      self.assertEquals(len(L),0)

    def test_incorrect(self):
      """
	Test that error is raised when we pass incorrect args
      """
      self.assertRaises(IndexError, a1.swap_k, [], -1)
      self.assertRaises(IndexError, a1.swap_k, [1,2], len([1,2])+1)

    def test_swap(self):
      """
	Test that error is raised when we pass incorrect args
      """
      L = [1,2,3]
      expected = [3,2,1]
      a1.swap_k(L, 1)
      self.assertEquals(L,expected)
      
      L = [1,2,3,4,5,6]
      expected = [5,6,3,4,1,2]
      a1.swap_k(L, 2)
      self.assertEquals(L,expected)
      


if __name__ == '__main__':
    unittest.main(exit=False)
