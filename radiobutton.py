from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:/Users/user/PycharmProjects/selenium_python/driver/chromedriver.exe")
time.sleep(5)
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

selection = driver.find_element(By.ID,"RESULT_RadioButton-7_1").is_selected()
print(selection)

displaying = driver.find_element(By.ID,"RESULT_RadioButton-7_1").is_displayed()
print(displaying)

driver.find_element(By.ID,"RESULT_RadioButton-7_1").click()