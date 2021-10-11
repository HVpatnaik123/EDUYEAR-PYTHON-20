from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="C:/Users/user/PycharmProjects/selenium_python/driver/chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# scroll down by pixel
# driver.execute_script("window.scrollBy(0,1000)","")

#scroll down till element is found
# element = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[56]/td[2]")
# driver.execute_script("argument[0].scrollIntoView():",element)

#scroll till end of webpage
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")