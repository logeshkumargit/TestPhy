'''
Created on Apr 8, 2020

@author: logesh.kumar
'''
from selenium.webdriver.common.by import By


class Login(object):
    '''
    classdocs
    '''
    user_name = (By.NAME, "UserName")
    password = (By.NAME,"password")
    signin = (By.NAME, "login")

def login(self):
    self.driver.fine_element(*self.user_name).send_keys("demo")
    self.driver.fine_element(*self.user_password).send_keys("demo")
    self.driver.fine_element(*self.signin).click()
    return self.driver.title

    def register(self):
    self.driver.fine_element(*self.email).send_keys("demo")
    self.driver.fine_element(*self.password).send_keys("demo")
    self.driver.fine_element(*self.confirmPassword).send_keys("demo") 
    self.driver.fine_element(*self.register).click()

 
    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver = driver