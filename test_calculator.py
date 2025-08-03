import unittest
from encodings import search_function

from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 2*3)
        self.assertEqual(mul(2, 0), 2*0)
        self.assertEqual(mul(2, -1), 2*-1)


    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 3), 3/2)
        self.assertEqual(div(2, 0), 0/2)
        self.assertEqual(div(-1, 2), 2/-1)



    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)



    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(2, 2), math.hypot(2,  2))
        self.assertEqual(hypotenuse(2, -2), math.hypot(-2, 2))
        self.assertEqual(hypotenuse(4, 2), math.hypot(4, -2))

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(1), math.sqrt(1))
        self.assertEqual(square_root(2), math.sqrt(2))
        self.assertEqual(square_root(0), math.sqrt(0))


        
            # Do not touch this
if __name__ == "__main__":
    unittest.main()