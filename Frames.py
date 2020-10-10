from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.get("https://www.selenium.dev/selenium/docs/api/java/")

driver.switch_to.frame("packageListFrame") #1st frame
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(5)

#go back to the main page
driver.switch_to.default_content()

#go to the 2nd frame
driver.switch_to.frame("packageFrame") #2nd frame
driver.find_element_by_link_text("WebDriver").click()
time.sleep(5)

#go back to the main page
driver.switch_to.default_content()
time.sleep(5)
#go to the 3rd frame
driver.switch_to.frame("classFrame") #2nd frame
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click()

