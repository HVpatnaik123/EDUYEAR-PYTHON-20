from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/user/PycharmProjects/selenium_python/driver/chromedriver.exe')

driver.get('https://en-gb.facebook.com/')

driver.implicitly_wait(10)
print(driver.title)
assert 'Facebook – log in or sign up' in driver.title
driver.find_element_by_name('email').send_keys('9040915238')
driver.find_element_by_name('pass').send_keys('9040915238')

