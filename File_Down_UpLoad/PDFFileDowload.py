import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

location = os.getcwd()

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    #serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
    #download files in desired location
    preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # selenium chrome use multiple add_experimental_option
    options.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(options=options)
    return driver

# def edge_setup():
#     from selenium.webdriver.edge.service import Service
#     #serv_obj = Service("C:\Drivers\edgedriver_win64\msedgedriver.exe")
#     #download files in desired location
#     preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
#     ops=webdriver.EdgeOptions()
#     ops.add_experimental_option("detach", True)
#     ops.add_experimental_option("prefs", preferences)
#     driver = webdriver.Edge(options=ops)
#     #driver = webdriver.Edge(service=serv_obj,options=ops)
#     return driver
#
# def firefox_setup():
#     from selenium.webdriver.firefox.service import Service
#     serv_obj = Service("C:\Drivers\geckodriver-v0.29.1-win64\geckodriver.exe")
#     #settings
#     ops=webdriver.FirefoxOptions()
#     ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")
#     ops.set_preference("browser.download.manager.showWhenStarting", False)
#     ops.set_preference("browser.download.folderList",2) #0-desktop 1-downloads folder 2- Desired loc
#     ops.set_preference("browser.download.dir",location)
#     ops.set_preference("pdfjs.disabled",True) # for pdf
#     driver = webdriver.Firefox(service=serv_obj,options=ops)
#     return driver

#Automation code
my_driver=chrome_setup()
#my_driver=edge_setup()
#driver=firefox_setup()

my_driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/") # //*[@id="table-files"]/tbody/tr[1]/td[5]/a
my_driver.maximize_window()
my_driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()

#alert = my_driver.switch_to.alert
#alert.dismiss()
