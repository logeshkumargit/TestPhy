'''
Created on Apr 8, 2020

@author: logesh.kumar
'''

from selenium.webdriver.common.by import By


class init(object):
    
def setUp(self):
        self.driver = webdriver.Chrome(
            "C:\\Users\\suman.palle\\Downloads\\SeleniumBroDrivers\\chromedriver.exe")
        self.driver.get("http://newtours.demoaut.com/mercurywelcome.php")
        self.driver.maximize_window()
        print(self.driver.title)

 

    def tearDown(self):
        # self.driver.quit()
        print("after test")

 

    def testName(self):
        self.lp = LoginT(self.driver)
        self.lp.login()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()