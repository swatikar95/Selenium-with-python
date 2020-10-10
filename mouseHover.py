from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.get('http://opensource-demo.orangehrmlive.com')

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input").click()

admin=driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[1]/a/b")
user_management=driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/a")
user=driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/ul/li/a")

actions=ActionChains(driver)

actions.move_to_element(admin).move_to_element(user_management).move_to_element(user).click().perform()