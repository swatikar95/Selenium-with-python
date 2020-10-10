from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/checkboxes")

driver.find_element_by_id("checkboxes").click()