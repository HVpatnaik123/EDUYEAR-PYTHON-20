from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/user/PycharmProjects/selenium_python/driver/chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()
driver.switch_to_frame("main")
# upload_file_path = "C:/Users/user/Downloads/IMG_20210418_0005"
# driver.find_element_by_name("RESULT_FileUpload-10").click()

driver.find_element_by_xpath("//*[@id='RESULT_FileUpload-10']").send_keys("C:/Users/user/Downloads/IMG_20210418_0005")