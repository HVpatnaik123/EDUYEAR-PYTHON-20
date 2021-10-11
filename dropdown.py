from selenium.webdriver.support.ui import Select

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:/Users/user/PycharmProjects/selenium_python/driver/chromedriver.exe')
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
element = driver.find_element(By.ID,'RESULT_RadioButton-9')
element1 = Select(element)
#approach 1 using visible text
element1.select_by_visible_text("Morning")
#approach 2 using index
element1.select_by_index(2)
#Approach 3 select by value
element1.select_by_value('Radio-2')

# count number of elements in dropdown
print(len(element1.options))

#capture all the options
var_store = element1.options
for item in var_store:
    print(item.text)

