from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)


driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

coutrieslist=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(coutrieslist))

for country in coutrieslist:
    if country.text == "India":
        country.click()
        break