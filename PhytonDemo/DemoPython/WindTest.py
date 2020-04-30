'''
Created on Apr 7, 2020

@author: logesh.kumar
'''
from selenium import webdriver
driver = webdriver.Chrome(
    "C:\\Logesh\\Auto Sele\\chromedriver_win32\\chromedriver.exe")
driver.get('https://www.google.com/intl/en-GB/gmail/about/#')
# driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)
driver.find_element_by_link_text("Sign in")
print(driver.title)
driver.find_element_by_link_text("Terms").click()
print(driver.title)
whand = driver.window_handles
print(len(whand))
driver._switch_to.window(whand[1])
print(driver.title)
driver.find_element_by_link_text("Archived versions").click()