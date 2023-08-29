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
    preferences = {"download.default_directory": location}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # selenium chrome use multiple add_experimental_option
    options.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(options=options)


    #ops = webdriver.ChromeOptions()
    #driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver

# def edge_setup():
#     from selenium.webdriver.edge.service import Service
#     #serv_obj = Service("C:\Drivers\edgedriver_win64\msedgedriver.exe")
#     #download files in desired location
#     preferences={"download.default_directory":location}
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
#     ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
#     ops.set_preference("browser.download.manager.showWhenStarting", False)
#     ops.set_preference("browser.download.folderList",2) #0-desktop 1-downloads folder 2- Desired loc
#     ops.set_preference("browser.download.dir",location)
#     driver = webdriver.Firefox(service=serv_obj,options=ops)
#     return driver

#Automation code
my_driver=chrome_setup()
#my_driver=edge_setup()
#driver=firefox_setup()

my_driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/") # //*[@id="table-files"]/tbody/tr[1]/td[5]/a
my_driver.maximize_window()
my_driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()

my_driver.switch_to.frame(1)
#WebDriverWait(my_driver, 2).until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[starts-with(@id, 'ad_iframe')]"))) # //iframe[starts-with(@id, 'sp_message_iframe')]
logElement = my_driver.find_element((By.ID, "dismiss-button")) # //*[@id="dismiss-button"]
logElement.click()

#time.sleep(2)
#outerframe = my_driver.find_element((By.XPATH, "//*[@id='creative']")) # //*[@id="ad_iframe"]
#my_driver.switch_to.frame(outerframe)
#my_driver.switch_to.frame("Advertisement")
#my_driver.switch_to.alert.dismiss()

#my_frame = my_driver.find_element(By.ID, "creative")
#my_driver.switch_to.frame('creative')

#outerframe = my_driver.find_element((By.XPATH, "//*[@id='ad_iframe']")) # //*[@id="ad_iframe"]
#my_driver.switch_to.frame(outerframe)
#logElement = WebDriverWait(my_driver, 2).until(ec.presence_of_element_located((By.XPATH, "//*[@id='dismiss-button']"))) # //*[@id="dismiss-button"]
#logElement.click()

# my_driver.switch_to.default_content()  # go back to main page

#opens alert window


#my_driver.find_element(By.XPATH, "//*[@id='dismiss-button']").click()
#time.sleep(2)
#
#logElement.dismiss()



