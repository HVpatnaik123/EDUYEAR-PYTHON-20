from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("prefs",("download.default_directory":"download path"))

driver = webdriver.Chrome(executable_path="", chrome_options=chrome_options)