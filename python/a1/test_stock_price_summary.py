import a1
import unittest
import math

class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. 
	assertAlmostEqual is used because of floating
	point comparison
    """

    
    def test_empty(self):
        """
	  Test if we have correct result in case of
	  empty list
        """
        (gains, losses) = a1.stock_price_summary([])
        self.assertAlmostEqual(gains, 0.0)
        self.assertAlmostEqual(losses, 0.0)
        
    def test_gains(self):
        """
	  Test we get correct result for gains only
        """
        g = [0.3, 0.3, 0.3, 0.1]
        (gains, losses) = a1.stock_price_summary(g)
        self.assertAlmostEqual(gains, math.fsum(g))

    def test_losses(self):
        """
	  Test that we get correct result for losses	  
        """
        g = [-0.3, -0.3, -0.3, -0.1]
        (gains, losses) = a1.stock_price_summary(g)
        self.assertAlmostEqual(losses, math.fsum(g))
        
    def test_all(self):
        """
	  Test that we get correct result for losses
	  and gains
        """
        g = [-0.3, 0.3, -0.3, 0.3, 0.0]
        (gains, losses) = a1.stock_price_summary(g)
        self.assertAlmostEqual(losses, -0.6)
        self.assertAlmostEqual(gains, 0.6)
        


if __name__ == '__main__':
    unittest.main(exit=False)
