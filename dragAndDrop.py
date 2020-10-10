from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.get("http://the-internet.herokuapp.com/drag_and_drop")

source_element=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]")
target_element=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]")

actions=ActionChains(driver)

actions.drag_and_drop(source_element,target_element).perform()

