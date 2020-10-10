from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")

driver.get("http://the-internet.herokuapp.com/tables")


#count no. of rows in the table
rows=len(driver.find_elements_by_xpath("/html/body/div[2]/div/div/table[1]/tbody/tr"))
print(rows)

#count no. of columns
columns=len(driver.find_elements_by_xpath("/html/body/div[2]/div/div/table[1]/tbody/tr[1]/td"))
print(columns)

#read all the value of row and col
for r in range(2,rows+1):
    for c in range(1,columns+1):
        value=driver.find_element_by_xpath("/html/body/div[2]/div/div/table[1]/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end='    ')
    print()
