import unittest

class Test(unittest.TestCase):
    #func will start with test_
    def test_firsttest(self):
        print("This is my 1st case")

if __name__=="__main__":
    unittest.main()