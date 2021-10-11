
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:/Users/user/PycharmProjects/selenium_python/driver/chromedriver.exe")

driver.get('https://www.facebook.com/')
username = driver.find_element_by_name('email')
print(username.is_enabled())
print(username.is_displayed()) #check whether email is displayed or not
username.send_keys('9040915238')
pswd = driver.find_element_by_name('pass')
print(pswd.is_displayed())
pswd.send_keys('Harsha.1234')

# driver.find_element_by_name('login').click()

try:
    driver.find_element_by_xpath('//*[@id="u_0_a_H3"]/div[3]/a').click()
except:
    print('there is some  issue')

driver.close()
