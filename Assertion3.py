#assertIsNone verifies whether given values are None or not,if None, it passes

import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def testName(self):
        driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")
        # self.assertIsNone(driver) #vrifies whether there is any value or not,if it has value, returns false
        self.assertIsNotNone(driver) #returns True

        # driver=None
        # self.assertIsNone(driver) #vrifies whether there is any value or not,if it has value, returns false


if __name__ == "__main__":
    unittest.main()