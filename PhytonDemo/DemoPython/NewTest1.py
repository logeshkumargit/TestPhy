'''
Created on Apr 8, 2020

@author: logesh.kumar
'''
import unittest

class NewTest1(unittest.TestCase):
    
    def testName1(self):
        print("test name1")
        pass
    def testName2(self):
        print("test name2")
        
if __name__ == "__main__":
    unittest.main()