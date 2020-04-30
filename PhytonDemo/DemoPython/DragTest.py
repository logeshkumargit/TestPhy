'''
Created on Apr 7, 2020

@author: logesh.kumar
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
d= webdriver.Chrome(
    "C:\\Logesh\\Auto Sele\\chromedriver_win32\\chromedriver.exe")
d.get("http://jqueryui.com")
d.implicitly_wait(5000)
d.maximize_window()
d.find_element_by_link_text("Droppable").click()
d.switch_to_frame(0)
drag = d.find_element_by_id("draggable")
drop = d.find_element_by_id("droppable")
ActionChains(d).drag_and_drop(drag, drop).perform()
d.switch_to_default_content()
d.find_element_by_link_text("Menu").click()
d.switch_to_frame(0)
action = ActionChains(d)
d.find_element_by_id("ui-id-4").click()
firstLevelMenu = d.find_element_by_id("ui-id-4")
action.move_to_element(firstLevelMenu).perform()
secondLevelMenu = d.find_element_by_id("ui-id-6")
action.move_to_element(secondLevelMenu).perform()



