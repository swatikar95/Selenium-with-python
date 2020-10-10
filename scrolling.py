from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.get("https://phptravels.com/tours-module-features/")

driver.maximize_window() #maximize window

#1.scroll 0 position to 1000pixel position
#driver.execute_script("window.scrollBy(0,1000)","")

#2.scroll down accoring to find some element
# flag=driver.find_element_by_xpath("/html/body/div[3]/main/section[2]/div[1]/img")
# driver.execute_script("arguments[0].scrollIntoView();",flag)

#3.scrollpage till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")