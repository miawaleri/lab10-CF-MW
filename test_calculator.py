import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(12,13), 12+13)
        self.assertEqual(add(9,0), 9+0)
        self.assertNotEqual(add(2,7), 2+8)



    def test_subtract(self): # 3 assertions
         self.assertEqual(sub(119,12), 119-12)
         self.assertEqual(sub(-119,12), -119-12)
         self.assertNotEqual(sub(12,0), 12-1)
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
             div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(9,19), math.log(19,9))
        self.assertEqual(log(2,3), math.log(3,2))
        self.assertEqual(log(-2,3), math.log(3,-2))


    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            log(0, 5)
    ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()