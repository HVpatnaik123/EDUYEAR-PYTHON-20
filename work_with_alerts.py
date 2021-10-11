from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:/Users/user/PycharmProjects/selenium_python/driver/chromedriver.exe")

driver.get('https://testautomationpractice.blogspot.com/')

driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)
#to close alert using ok button
# driver.switch_to_alert().accept()

#to close button using cancel button
driver.switch_to_alert().dismiss()

driver.quit()