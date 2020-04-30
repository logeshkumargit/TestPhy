'''
Created on Apr 7, 2020

@author: logesh.kumar
'''
# Register

 
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from _operator import contains
driver = webdriver.Chrome(
    "C:\\Logesh\\Auto Sele\\chromedriver_win32\\chromedriver.exe")
driver.get('http://newtours.demoaut.com/')
driver.maximize_window()
driver.implicitly_wait(10)
lnk_coll = driver.find_elements_by_tag_name("a")
print(len(lnk_coll))
for lnk_name in lnk_coll:
    print(lnk_name.text)
    if lnk_name.text == "REGISTER":
        lnk_name.click()
        break
        sel = Select(driver.find_element_by_name("country"))
        sel.select_by_value("11")
        sel.select_by_visible_text("INDIA")
        driver.find_element_by_name("email").send_keys("Piper")
        driver.find_element_by_name("password").send_keys("David")
        driver.find_element_by_name("confirmPassword").send_keys("David")
        driver.find_element_by_name("register").click()
        reg_sts = driver.find_element_by_xpath(
            "//table[1]/tbody[1]/tr[3]/td[1]/p[3]/a[1]/font[1]/b[1]").text
        print(reg_sts)
        if reg_sts == "Note: Your user name is Piper.":
            print("Registration success")
            driver.find_element_by_link_text("Home").click()
        else:
            print("Registration failed")
        driver.find_element_by_name("userName").send_keys("Piper")
        driver.find_element_by_name("password").send_keys("David")
        driver.find_element_by_name("login").click()

 

    elif lnk_name.text == "Cruises":
        lnk_name.click()
        tab_ele = driver.find_element_by_xpath(
            "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/th/table")
        tab_row_coll = tab_ele.find_elements_by_tag_name("tr")
        print(len(tab_row_coll))
        for trow in tab_row_coll:
            print(trow.text)
        break