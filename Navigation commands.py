import time

from selenium import webdriver
#from selenium.webdriver.common.keys import keys

driver = webdriver.Chrome(executable_path='C:/Users/user/PycharmProjects/selenium_python/driver/chromedriver.exe')

driver.get('https://www.google.com/')   #1st page
print(driver.title) #title for first url

time.sleep(5)
driver.get('https://www.facebook.com/') #2nd page
print(driver.title)     #title of 2nd page

driver.get('http://advantageonlineshopping.com/#/')
print(driver.title)

driver.back()
driver.back()   #goback to previous site
time.sleep(5)
print(driver.title) #title for first url

driver.forward()    #forward to new page
time.sleep(5)
print(driver.title)     #title of 2nd page

driver.quit()