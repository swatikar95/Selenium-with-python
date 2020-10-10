from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")
driver.get("http://book.theautomatedtester.co.uk/chapter1")

#working with radio buttons
status=driver.find_element_by_id("radiobutton").is_selected()
print("previously",status)

driver.find_element_by_id("radiobutton").click() #selects radio button

status=driver.find_element_by_id("radiobutton").is_selected()
print("After Clicking:",status)
