'''
Created on Apr 6, 2020

@author: logesh.kumar
'''

# Choose = input("Enter your Browser, Chrome/IE")
# 
# 
# from selenium import webdriver
# if Choose == 'Chrome':
#         browser = webdriver.Chrome("C:\\Logesh\\Auto Sele\\chromedriver_win32\\chromedriver.exe")
#         browser.get('http://seleniumhq.org/')
# 
# elif Choose == 'IE':
#          browser = webdriver.Ie("C:\\Logesh\\Auto Sele\\IEDriverServer_x64_3.150.1\\IEDriverServer.exe")
#          browser.get('https://seleniumhq.org/')
#          
         
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(
    "C:\\Logesh\\Auto Sele\\chromedriver_win32\\chromedriver.exe")
driver.get('http://demowebshop.tricentis.com/')
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)

# Register
driver.find_element_by_link_text("Register").click()
# driver.find_element_by_name("country").send_keys("TOGO")
driver.find_element_by_id("gender-male").click()
driver.find_element_by_name("FirstName").send_keys("Test")
driver.find_element_by_name("LastName").send_keys("Test")
driver.find_element_by_name("Email").send_keys("TestingTesting7@testing.com")
driver.find_element_by_name("Password").send_keys("Test123")
driver.find_element_by_name("ConfirmPassword").send_keys("Test123")
driver.find_element_by_id("register-button").click()
reg_sts = driver.find_element_by_xpath(
    "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]").text
print(reg_sts)
if reg_sts == "Your registration completed":
    print("Registration success")
    driver.find_element_by_link_text("Log out").click()
else:
    print("Registration failed")
driver.implicitly_wait(10)
time.sleep(3)
driver.find_element_by_link_text("Log in").click()
driver.find_element_by_name("Email").send_keys("TestingTesting7@testing.com")
driver.find_element_by_name("Password").send_keys("Test123")
driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input").click()
time.sleep(3)
driver.quit()