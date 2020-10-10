from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.get("http://swisnl.github.io/jQuery-contexMenu/demo.html")

button=driver.find_element_by_xpath("")

actons=ActionChains(driver)
#right click action
actons.context_click(button).perform()