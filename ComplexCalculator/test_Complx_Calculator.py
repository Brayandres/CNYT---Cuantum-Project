import unittest
import Complx_Calculator

class Test_Complx_Calculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(print(Cartesian((1, 4))+Cartesian((-5, -1))), "(-4, -3)")

if __name__ == "__main__":
    unittest.main()
