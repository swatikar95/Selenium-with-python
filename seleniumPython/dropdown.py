from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.get("http://book.theautomatedtester.co.uk/chapter1")

element=driver.find_element_by_id("selecttype")
drp=Select(element)

#selecting by text
drp.select_by_visible_text("Selenium IDE")

#selecting by index
drp.select_by_index(2)

#count number of options
print(len(drp.options))

#capture all the options and print
all_options=drp.options
for option in all_options:
    print(option.text) #from option, we need t extract text values