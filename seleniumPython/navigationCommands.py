from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html") #open this browser

print(driver.title) #print the title

driver.get("https://colab.research.google.com/notebooks/intro.ipynb#recent=true") #open another browser
time.sleep(5) #remains 5 sec

print(driver.title) #print title

driver.back() #back to the 1st browser

time.sleep(5) #sleps 5 sec

print(driver.title) #prints title

driver.forward() #forward to the nest browser

print(driver.title) #prints title

driver.quit()
