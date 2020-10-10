#assertIn varifies whether 1st element is present in the seconf lement or not
# verifiy presence in list,tuple,set,dictionary

import unittest

class Test(unittest.TestCase):
    def testName(self):
        list=['Python','Selenium','Java']

        # self.assertIn("Python",list) #return true
        self.assertNotIn("python",list) #return true


if __name__ == "__main__":
    unittest.main()