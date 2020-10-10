#it is a check point to know whether a test case is failed or not
#assertEqual compares 1t parameter with 2nd parameter,if matches,reamining execution will done
#assertNotEqual compares 2 parameters,if not same,unittest passes test case

import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")
        driver.get("https://www.google.com/")
        #title captures from website
        titleOfWebPage=driver.title
        #title expecting,if matches,it will pass
        # self.assertEqual("Google",titleOfWebPage,"webpage title is not same")
        # self.assertEqual("Google123", titleOfWebPage, "webpage title is not same")
        # self.assertNotEqual("Google123", titleOfWebPage, "webpage title is not same")
        self.assertNotEqual("Google", titleOfWebPage, "webpage title is same")



if __name__ == "__main__":
    unittest.main()

