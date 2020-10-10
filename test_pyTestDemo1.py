import pytest

# pytest.fixture executes specific method before every testmethod
@pytest.fixture()
def setup():
    print("Once before every method")

def testMethod1(setup):
    print("test method 1")

def testMethod2(setup):
    print("test method 2")