from selenium import webdriver



driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.get("http://newtours.demoaut.com/") #URL taking much times

#inplicit wait affects all the elements of the page
#time based;if not shown in the given time, raise exception
driver.implicitly_wait(10) #functions of this page maximum wait 10 sec

assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("passward").send_keys("mercury")

driver.find_element_by_name("login").click()
