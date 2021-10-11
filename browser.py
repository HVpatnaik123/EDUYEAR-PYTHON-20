from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='C:/Users/user/PycharmProjects/selenium_python/driver/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://www.google.com/')
print(driver.title) #returns title of the page
print(driver.current_url)   #returns url of the page

#to search element using xpath
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]').click()
print(driver.current_url)   #returns url of the page
print(driver.page_source)

driver.implicitly_wait(10)
driver.close()  #close one browser at a time (1st url)
driver.quit()   #close all the tabs in browser