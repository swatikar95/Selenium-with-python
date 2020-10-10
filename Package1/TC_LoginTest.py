import unittest

class LoginTest(unittest.TestCase):
    def test_loginbyEmail(self):
        print("This is login by email")
        self.assertTrue(True)

    def test_loginbyFacebook(self):
        print("This is login by facebook")
        self.assertTrue(True)

    def test_loginbyTwitter(self):
        print("This is login by twitter")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()