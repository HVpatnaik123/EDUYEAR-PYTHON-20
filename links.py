from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='C:/Users/user/PycharmProjects/selenium_python/driver/chromedriver.exe')

driver.get('https://www.expedia.co.in/')
links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))   #to print the no. of links

#to capture the links
for item in links:
    print(item.text)

#to click on a specific link
# driver.find_element(By.LINK_TEXT,"Packages").click()    # using link test
capture_title = driver.title
print(capture_title)

driver.find_element(By.PARTIAL_LINK_TEXT,"Pack").click()    # using link test
# driver.quit()