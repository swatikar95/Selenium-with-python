from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("http://www.expedia.com/")

#explicit wait is condition based
# only functions that will cover conditions, will work
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/figure/div[3]/div/div/div/ul/li[2]/a/span").click() #clicks flight button

time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/figure/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/div/button[1]").send_keys("SFO")
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/figure/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div/button[1]").send_keys("NYC")
#
# driver.find_element_by_id("d1-btn").clear() #clears previous values if any given
# driver.find_element_by_id("d1-btn").send_keys("Oct 16")
# driver.find_element_by_id("d2-btn").clear()
# driver.find_element_by_id("d2-btn").send_keys("Oct 17")
#
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/figure/div[3]/div/div/div/div/div[1]/div/form/div[3]/div[2]/button").click()
# #explicit wait statements
# #time defines it will wait max 10 min for element event to occur
# wait=WebDriverWait(driver,10)
# element = wait.until(EC.element_to_be_clickable(""))
# element.click()
# time.sleep(3)
#
# driver.quit()