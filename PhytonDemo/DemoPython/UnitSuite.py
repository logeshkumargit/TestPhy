'''
Created on Apr 8, 2020

@author: logesh.kumar
'''

import unittest
import HtmlTestRunner

from DemoPython import NewTest1
from DemoPython import NewTest2


suite=unittest.TestSuite()

suite.addTest(NewTest1('testName1'))
suite.addTest(NewTest1('testName2'))
suite.addTest(NewTest2('testName3'))
suite.addTest(NewTest2('testName4'))

 
#unittest.TextTestRunner().run(suite)
my_runner=HtmlTestRunner.HTMLTestRunner(output='test-reports',report_title='Test Report')
my_runner.run(suite)