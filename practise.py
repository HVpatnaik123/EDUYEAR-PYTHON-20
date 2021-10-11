
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome(executable_path= 'C:/Users/user/PycharmProjects/selenium_python/driver/chromedriver.exe')
driver.maximize_window()
# driver.get('https://www.google.com')
# print(driver.title)
# driver.get('https://www.facebook.com/')
# print(driver.title)
# driver.back()
# print('google',driver.title)
# driver.forward()
# print('fb',driver.title)
#
# print(driver.current_url)
# print(driver.page_source)
# driver.close()


# user_ele = driver.find_element_by_name('email')
# print(user_ele.is_displayed())
# print(user_ele.is_enabled())
# user_ele.send_keys('harsha patnaik')
# pswd_ele = driver.find_element_by_css_selector("input[id=pass]")
# pswd_ele.send_keys('Harsha')

# implicit wait
# driver.implicitly_wait(5)
# assert "Facebook – log in or sign up" in driver.title
# user_ele = driver.find_element_by_name('email')
# print(user_ele.is_displayed())
# print(user_ele.is_enabled())
# user_ele.send_keys('harsha patnaik')
# pswd_ele = driver.find_element_by_css_selector("input[id=pass]")
# pswd_ele.send_keys('Harsha')

# explicit wait
# driver.get('https://www.expedia.co.in/')
#
# driver.implicitly_wait(5)
# assert 'Expedia Travel: Vacations, Cheap Flights, Airline Tickets & Airfares' in driver.title
# driver.find_element(By.XPATH, '//*[@id="uitk-tabs-button-container"]/li[2]/a/span').click()
# driver.find_element(By.XPATH,'//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[1]/div/div[1]/div/div/div/button').click()
# driver.find_element_by_xpath('//*[@id="app-layer-location-field-leg1-origin-ta-dialog"]/div[2]/div/div[1]/section/div/input').send_keys('SFO')
# driver.find_element_by_xpath('//*[@id="app-layer-location-field-leg1-origin-ta-dialog"]/div[2]/div/div[2]/ul/li[1]/button/div/div[1]/span/strong').click()
# #
# # driver.find_element(By.XPATH, '//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[1]/div/div[2]/div/div/div/button').send_keys('nyc')
# # driver.find_element_by_xpath('//*[@id="wizard-flight-pwa-1"]/div[3]/div[2]/button').click()
#
#

# working with input boxes,radio buttons & check boxes
# driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
# inp_boxex = driver.find_elements(By.CLASS_NAME,"text_field")
# print(len(inp_boxex))
#
# driver.find_element(By.NAME,'RESULT_TextField-1').send_keys('Harsha Vardhan')
# driver.find_element(By.ID,'RESULT_TextField-2').send_keys('Patnaik')

# print("displayed: ",driver.find_element_by_css_selector("input[Radio-0]").is_displayed())
# print("selected: ",driver.find_element_by_css_selector("input[Radio-0]").is_selected())
# print("enabled: ",driver.find_element_by_css_selector("input[Radio-0]").is_enabled())
# driver.find_element_by_css_selector("input[Radio-0]").click()
# print("selected: ",driver.find_element_by_css_selector("input[Radio-0]").is_selected())
# stat = driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()
# print(stat)
# button = driver.find_element_by_id('RESULT_RadioButton-7_0').click()
#
# stat1 = driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()
# print(stat1)

# working with dropdowns

# drop_down = driver.find_element(By.NAME,"RESULT_RadioButton-9")
# sel_obj = Select(drop_down)
#
# sel_obj.select_by_visible_text('Morning')
# sel_obj.select_by_index(2)
# sel_obj.select_by_value('Radio-2')
#
# print(len(sel_obj.options))
# a = []
# list_options = sel_obj.options
# for i in list_options:
#     print(a.append(i.text))
# print(a)


# working with links:

# driver.get('https://www.facebook.com/')
# links1 = driver.find_elements(By.TAG_NAME,'a')
# print(len(links1))
# for i in links1:
#     print(i.text)
#
# # driver.find_element(By.LINK_TEXT,"Sign Up").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Sign").click()

# working with alerts
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()
# # driver.switch_to_alert().accept()
# driver.switch_to_alert().dismiss()

# working with frames:
# driver.get('https://seleniumhq.github.io/selenium/docs/api/java/index.html')
# driver.find_element_by_xpath('/html/body/header/nav/div[1]/div[2]/ul[1]/li[1]/a').click()
#
# driver.switch_to.frame('packageListFrame')
# driver.find_element(By.LINK_TEXT,"org.openqa.selenium.cli").click()
# driver.back()
# driver.find_element_by_xpath('/html/body/header/nav/div[1]/div[2]/ul[1]/li[1]/a').click()
# driver.switch_to.default_content()
# driver.switch_to.frame('packageFrame')
# driver.find_element_by_xpath('/html/body/main/ul/li[11]/a').click()

# working with browser windows:

# driver.get('http://demo.automationtesting.in/Windows.html')
# print(driver.current_window_handle)
# driver.find_element(By.XPATH,'//*[@id="Tabbed"]/a/button').click()
# print(driver.current_window_handle) #CDwindow-A1724158F86144109DD380B0251C9579-parent
# store= driver.window_handles
# for i in store:
#     print(driver.switch_to.window(i))
#     print(driver.title)
#     if driver.title == 'SeleniumHQ Browser Automation':
#         driver.close()

# scrolling webpages:
# driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
# driver.maximize_window()

# driver.execute_script("window.scrollBy(0,10000)","")
# User_Element = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[2]/tbody/tr[60]/td[2]")
# driver.execute_script("arguments[0].scrollIntoView();", User_Element)

# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

# mouse Actions
# mouse hover
# driver.get('https://opensource-demo.orangehrmlive.com')
# driver.maximize_window()
#
# driver.find_element(By.ID,"txtUsername").send_keys('Admin')
#
# driver.find_element(By.ID,"txtPassword").send_keys('admin123')
#
# driver.find_element(By.ID,"btnLogin").click()
#
# admin = driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
# userm = driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
# user = driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')
#
# actions = ActionChains (driver)
#
# actions.move_to_element(admin).move_to_element(userm).move_to_element(user).click().perform()

# double click:
# driver.get('https://testautomationpractice.blogspot.com/')
# driver.maximize_window()
#
# doub = driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')
#
# actions = ActionChains(driver)
# actions.move_to_element(doub).double_click().perform()

# right click:

# driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
# driver.maximize_window()
#
# righty = driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')
#
# actions = ActionChains(driver)
# actions.context_click(righty).perform()
#
# driver.find_element_by_xpath('/html/body/ul/li[7]/span').click()
# driver.switch_to_alert().accept()

# drag & drop:
# driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
# driver.maximize_window()
#
# drag_source = driver.find_element_by_id('box6')
# drop_target = driver.find_element_by_id('box101')
#
# actions = ActionChains(driver)
#
# actions.drag_and_drop(drag_source,drop_target).perform()
#

#upload files
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
#
# driver.switch_to.frame(0)
# driver.find_element_by_name("RESULT_FileUpload-10").click().send_keys("IMG_20170920_124830-1.jpg")
#
# time.sleep(10)
# driver.close()
# driver.quit()
