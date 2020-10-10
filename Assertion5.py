#assertGreater verifies whether 1st value is greater than 2nd value or not
#assertGreaterEqual verifies 1st parameter is geater or equal to 2nd parameter

import unittest

class Test(unittest.TestCase):
    def testName(self):
        # self.assertGreater(100,10) #will pass
        # self.assertGreaterEqual(10,10) #will pass
        # self.assertLess(10,100) #will pass
        self.assertLessEqual(10,10)


if __name__ == "__main__":
    unittest.main()