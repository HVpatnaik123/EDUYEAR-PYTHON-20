from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:/Users/user/PycharmProjects/selenium_python/driver/chromedriver.exe")
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

driver.maximize_window()

click_me = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

actions = ActionChains(driver)

actions.context_click(click_me).perform()

