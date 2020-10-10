from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.switch_to_frame(0)

driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C://image/Apple_logo_black.svg")