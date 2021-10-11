from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:/Users/user/PycharmProjects/selenium_python/driver/chromedriver.exe")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()
source_box = driver.find_element_by_xpath("//*[@id='box1']")

destination_box = driver.find_element_by_xpath("//*[@id='box103']")

actions = ActionChains(driver)

actions.drag_and_drop(source_box, destination_box).perform()