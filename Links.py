from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.get("http://book.theautomatedtester.co.uk/")

#links always remain in the attribute "a"
links=driver.find_elements_by_tag_name("a")

#count how many links in the page
print("Number of links present",len(links))

#read every links
for link in links:
    print(link.text)

#click the links
#method 1
#driver.find_element_by_link_text("Chapter1").click()

#method 2
driver.find_element_by_partial_link_text("Cha").click()
