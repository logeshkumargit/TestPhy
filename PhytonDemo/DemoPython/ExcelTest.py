'''
Created on Apr 8, 2020

@author: logesh.kumar
'''
import openpyxl
from selenium import webdriver
from selenium.webdriver.support.ui import Select

 

'loading the workbook'
workbook = openpyxl.load_workbook("C:\\Logesh\\Auto Sele\\ExcelTest.xlsx")
'connecting to worksheet'
wsheet = workbook.get_sheet_by_name("Data")
'work sheet rows and columns'
cells = wsheet['A2':'B4']
d = webdriver.Chrome(
    "C:\\Logesh\\Auto Sele\\chromedriver_win32\\chromedriver.exe")
d.get("http://newtours.demoaut.com/")
for c1, c2 in cells:
    print(c1.value, c2.value)
    d.implicitly_wait(5)
    print(d.title)
    d.maximize_window()
    str_enable = d.find_element_by_link_text("REGISTER").is_enabled()
    print(str_enable)
    d.find_element_by_link_text("REGISTER").click()
    sel = Select(d.find_element_by_name("country"))
    sel.select_by_index(2)
    sel.select_by_value("4")
    d.find_element_by_name("email").send_keys(c1.value)
    d.find_element_by_name("password").send_keys(c2.value)
    d.find_element_by_name("confirmPassword").send_keys(c2.value)
    d.find_element_by_name("register").click()
    sts_msg = d.find_element_by_xpath(
        "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[3]/a/font/b").text
    print(sts_msg)
    if sts_msg == "Note: Your user name is mary.":
        print("Registration is success")
    else:
        print("Registration is failed")