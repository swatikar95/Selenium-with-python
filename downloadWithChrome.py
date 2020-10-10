from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#to download files in specific location
chromeOptions=Options()
chromeOptions.add_experimental_option("prefs",{"download.default_dict":"c:/downloadfiles"})



driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe",chrome_options=chromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

#download text file
driver.find_element_by_id("textbox").send_keys("testing download of text file")
driver.find_element_by_id("createTxt").click()
#download
driver.find_element_by_id("link-to-download").click()

#download pdf
driver.find_element_by_id("pdfbox").send_keys("testing pdf")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()
