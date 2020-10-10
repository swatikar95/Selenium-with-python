import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturnTest import PaymentReturnTest

# get all tests from LoginTest, SignupTest, PaymentTest, PaumentReturnTest
Tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
Tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
Tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
Tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

#creating test suites
sanityTestSuite=unittest.TestSuite([Tc1,Tc2]) # sanity test suites
# unittest.TextTestRunner().run(sanityTestSuite)

functionalTestSuite=unittest.TestSuite([Tc3,Tc4]) #functional test suite
# unittest.TextTestRunner().run(functionalTestSuite)

masterTestSuite=unittest.TestSuite([Tc1,Tc2,Tc3,Tc4]) #master test suite
# unittest.TextTestRunner().run(masterTestSuite)
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)