import unittest

class Apptesting(unittest.TestCase):
    @unittest.SkipTest #method1
    def test_search(self):
        print("This is a search test")
    @unittest.skip("I am skipping it bcz it is nt ready yet") #method2
    def test_advancedsearch(self):
        print("This is an advanced search test")

    @unittest.skipIf(1==1,"Not Ready") #method3
    def test_prepaidRecharge(self):
        print("This is a prepaid recharge test")

    def test_postpaidRecharge(self):
        print("This is a postpaid recharge test")

    def test_loginbyemail(self):
        print("This is login by email")

    def test_loginbytwitter(self):
        print("This is login by twitter")

if __name__ == "__main__":
    unittest.main()
