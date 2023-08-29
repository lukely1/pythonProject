from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notificatins")
ops.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=ops)

#serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

#driver=webdriver.Chrome(service=serv_obj, options=ops)

driver.get("https://whatmylocation.com/")
driver.maximize_window()
