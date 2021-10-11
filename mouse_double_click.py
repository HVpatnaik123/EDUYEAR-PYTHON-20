from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:/Users/user/PycharmProjects/selenium_python/driver/chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

copy_text = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions = ActionChains(driver)

actions.double_click(copy_text).perform()
time.sleep(5)
driver.quit()
