from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.get("http://www.amazon.in/")

# #capture all the cookies created by browser
# cookies=driver.get_cookies()
# print(len(cookies))
# #print all cookie value pair
# print(cookies)

#adding new cookie to the browser
cookie={'name':'Mycookie','value':'123456'}
driver.add_cookie(cookie)

cookies=driver.get_cookies()
print(len(cookies))
#print all cookie after adding a new cookie
print(cookies)

#deleting cookie
driver.delete_cookie('Mycookie')
cookies=driver.get_cookies()
print(len(cookies))

#delete all cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))