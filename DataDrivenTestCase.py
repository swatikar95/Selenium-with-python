import XLutils
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.get("http://thedemosite.co.uk/login.php")
driver.maximize_window()

path="C://Users/HP/Google Drive/Learning/Selenium/xlFiles/LoginTest.xlsx"

rows=XLutils.getRowCount(path,"Sheet1")

for r in range(2,rows+1):
    username=XLutils.readData(path,"Sheet1",r,1)
    passward=XLutils.readData(path,"Sheet1",r,2)

    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(passward)
    driver.find_element_by_name("FormsButton2").click()

    # if driver.title=="Find a Flight:Tours":
    #     print("Test is passed")
    #     XLutils.writeData(path,"Sheet1",r,3,"test passed")
    # else:
    #     print("Test is failed")
    #     XLutils.writeData(path,"Sheet1",r,3,"test failed")
    #
    # driver.find_element_by_link_text("Home").click()

