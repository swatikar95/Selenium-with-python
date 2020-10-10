from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.get("https://phptravels.com/demo/")

#method1: taking ss
driver.save_screenshot("C://Users/HP/Google Drive/Learning/Selenium/ss/Demo.png")

#method2: taking ss
driver.get_screenshot_as_file("C://Users/HP/Google Drive/Learning/Selenium/ss/Demo1.png")
