from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")
# driver = webdriver.ie(executable_path=r"C:\Users\HP\Desktop\Learning\QA\IE\IEDriverServer.exe")

driver.get("https://colab.research.google.com/notebooks/intro.ipynb#recent=true")

print(driver.title)   #title of the page

print(driver.current_url)

# print(driver.page_source)   #HTML code for the page

driver.close()  # closes the browser