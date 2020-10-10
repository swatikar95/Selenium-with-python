from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button").click()

#sleep will kep popup window 5 sec
time.sleep(5)

#driver.switch_to_alert().accept()

driver.switch_to_alert().dismiss()
