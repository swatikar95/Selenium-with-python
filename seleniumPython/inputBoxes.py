from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.get("https://www.facebook.com/people/%E0%A6%B8%E0%A7%8D%E0%A6%AC%E0%A6%BE%E0%A6%A4%E0%A7%80-%E0%A6%95%E0%A6%B0/100009757590105")

#finding how many input boxes in the page
inputboxes=driver.find_elements_by_class_name("inputtext login_form_input_box")
print(len(inputboxes))

#how to provide value into the text box
driver.find_element_by_id("email").send_keys("swati54@gmail.com")

#find the status whether input value is displayed or not
status=driver.find_element_by_id("email").is_displayed()
print(status)
