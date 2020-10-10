#assertTrue mthod cheks whether 2 paramets are true or not,if true,test passes
#assertFalse mthod cheks whether 2 paramets are false or not,if false,test passes

import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")
        driver.get("https://www.google.com/")
        titleOfWebPage=driver.title

        # self.assertTrue(titleOfWebPage == "Google") #True
        # self.assertTrue(titleOfWebPage == "Google12") #False
        # self.assertFalse(titleOfWebPage == "Google") #False
        self.assertFalse(titleOfWebPage == "Google123") #True




    if __name__ == "__main__":
        unittest.main()
