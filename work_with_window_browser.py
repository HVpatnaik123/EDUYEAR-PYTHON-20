from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="C:/Users/user/PycharmProjects/selenium_python/driver/chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click()
print(driver.current_window_handle)

handler = driver.window_handles
for handle in handler:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "SeleniumHQ Browser Automation":
        driver.close()
# driver.quit()
