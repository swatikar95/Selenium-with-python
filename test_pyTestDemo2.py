import pytest

# pytest.yield_fixture executes specific method before and after every testmethod
@pytest.yield_fixture()
def setup():
    print("Once before every method")
    yield
    print("Once after every method")

def testMethod1(setup):
    print("test method 1")

def testMethod2(setup):
    print("test method 2")