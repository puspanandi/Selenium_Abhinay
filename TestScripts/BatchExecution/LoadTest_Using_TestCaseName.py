import unittest
# get all tests from SearchText and HomePageTest class
#from TestScripts.UnitTest_Example.UnitTest_Assertions import Assertions_Example_Boolean
from TestScripts.UnitTest_Example.UnitTest_Decorator import Draganddrop
from TestScripts.UnitTest_Example.UnitTest_Decorator.UnitTest_Setup_TearDown import SearchText
from TestScripts.UnitTest_Example.UnitTest_Assertions import Assertions_assertIs_OrangeHRM

#drag_drop = unittest.TestLoader().loadTestsFromName(Assertions_Example_Boolean.SimpleTest.test3(Assertions_Example_Boolean))
#drag_drop = unittest.TestLoader().loadTestsFromName(Draganddrop.SimpleTest.test_dd(Draganddrop))
search_text = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromModule(Assertions_assertIs_OrangeHRM)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)
