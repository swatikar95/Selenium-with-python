import unittest

#will execute before any cls or method present in test class
def setUpModule():
    print("setUpModule")
#will execute after any cls or method present in test class
def tearDownModule():
    print("tearDownModule")


class AppTesting(unittest.TestCase):
    #need to add an decoretor for setUp method
    @classmethod
    #this setUp method will execute before every test case
    def setUp(self):
        print("This is login test")
    
    @classmethod
    # this tearDown method will execute after every test case
    def tearDown(self):
        print("This is logout test")

    #setUp cls will exeute once before executing all test cases
    @classmethod
    def setUpClass(cls):
        print("Open application")

    #tearDown cls will exeute once after executing all test cases
    @classmethod
    def tearDownClass(cls):
        print("Close application")

    def test_search(self):
        print("This is a search test")

    def test_advancedsearch(self):
        print("This is an advanced search test")

    def test_prepaidRecharge(self):
        print("This is a prepaid recharge test")

    def test_postpaidRecharge(self):
        print("This is a postpaid recharge test")

if __name__=="__main__":
    unittest.main()