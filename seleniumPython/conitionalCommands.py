from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

user_element=driver.find_element_by_name("userName")

print(user_element.is_displayed()) #returns true/false based on element status
print(user_element.is_enabled()) #returns true/false

pass_element=driver.find_element_by_name("passward")

print(pass_element.is_displayed()) #returns true/false based on element status
print(pass_element.is_enabled()) #returns true/false

user_element.send_keys("mercury")
pass_element.send_keys("mercury")

driver.find_element_by_name("login").click()

roundtrip_radio=driver.find_element_by_css_selector("input[value=roundtrip]")
print("Status of round trip radio button",roundtrip_radio.is_selected()) #print status of radio button

onetrip_radio=driver.find_element_by_css_selector("input[value=onewayy]")
print("Status of oneway trip radio button",onetrip_radio.is_selected()) #print status of radio button
