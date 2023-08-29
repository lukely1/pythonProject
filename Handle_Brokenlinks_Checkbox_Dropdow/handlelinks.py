import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://demo.nopcommerce.com/")
#driver.maximize_window()

# click on link
#driver.find_element(By.LINK_TEXT,"Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

#Find number of links in a page
# links=driver.find_elements(By.TAG_NAME,'a')
links=driver.find_elements(By.XPATH, '//a')
print("total number of links:", len(links))

# print all the link names
for link in links:
    print(link.text)