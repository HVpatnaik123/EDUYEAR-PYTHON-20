from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait




driver = webdriver.Chrome(executable_path= 'C:/Users/user/'
                                           'PycharmProjects/selenium_python/driver/chromedriver.exe')
driver.maximize_window()
driver.get('https://www.expedia.co.in/')
print(driver.title)

time.sleep(5)   #python wait method
driver.find_element(By.XPATH,'//*[@id="uitk-tabs-button-container"]/li[2]/a/span').click()  #flight page
driver.find_element(By.XPATH,"//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[1]/div/div[1]/div/div/div/button").send_keys('NYC')
# driver.quit()