'''
Created on Apr 7, 2020

@author: logesh.kumar
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(
    "C:\\Logesh\\Auto Sele\\chromedriver_win32\\chromedriver.exe")
driver.get('http://newtours.demoaut.com/')
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)

# Register
driver.find_element_by_link_text("REGISTER").click()
# driver.find_element_by_name("country").send_keys("TOGO")
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
driver.find_element_by_link_text("Flights").click()
driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/b/font/input[2]").click()
driver.find_element_by_name("findFlights").click()
driver.find_element_by_name("reserveFlights").click()
driver.find_element_by_name("passFirst0").send_keys("Test")
driver.find_element_by_name("passLast0").send_keys("Test")
driver.find_element_by_name("creditnumber").send_keys("1234 5678 9012 3456")
driver.find_element_by_name("buyFlights").click()
conf = driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[3]/td/p/font/b/font[2]").text
print (conf)
if conf == "Your itinerary has been booked!":
    print("Booking done")
else:
    print("Booking failed")
driver.find_element_by_link_text("SIGN-OFF").click()
driver.quit()


