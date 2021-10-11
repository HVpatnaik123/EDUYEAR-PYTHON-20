from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:/Users/user/PycharmProjects/selenium_python/driver/chromedriver.exe")

driver.get("https://www.tutorialspoint.com/tutorialslibrary.htm")

#using frame 1
driver.switch_to.frame("academic_tutorials")
driver.find_element(By.LINK_TEXT,"CBSE Syllabus").click()
time.sleep(3)

driver.switch_to.default_content()  #to go back to main frame

#again start using a different frame using Name/Id/Index

driver.quit()