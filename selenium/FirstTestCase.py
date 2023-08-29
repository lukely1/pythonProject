# #1) Open Web Browser(Chrome/firefox/Edge).
# 2) Open URL  https://opensource-demo.orangehrmlive.com/
# 3) Enter username  (Admin).
# 4) Enter password  (admin123).
# 5) Click on Login.
# 6) Capture title of the home page.(Actual title)
# 7) Verify title of the page: OrangeHRM    (Expected)
# 8) close browser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec

# If the selenium version you are using is v4.6.0 or above (which I think it is as I see SeleniumManger in the error trace), then you don't really have to set the driver.exe path. Selenium can handle the browser and drivers by itself.
#
# So your code can be simplified as below:
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()

# driver = webdriver.Chrome("C:/Drivers/chromedriver.exe") //us

# from selenium.webdriver.chrome import options


# driver = webdriver.Chrome()

#options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)
# driver = webdriver.Chrome("C:/Drivers/chromedriver.exe")

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()


#serv_object = Service("C:/Drivers/msedgedriver.exe")
#options = webdriver.EdgeOptions()
#options.add_experimental_option("detach", True)
#driver = webdriver.Edge(service=serv_object, options=options)

#serv_object = Service("C:/Drivers/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/")

try:
    userNameElement= WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.NAME, "username")))
    userNameElement.send_keys('Admin')
    pwdElement = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.NAME, "password")))
    pwdElement.send_keys('admin123')
    logElement = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")))
    logElement.click()
finally:
    #driver.quit()
# pwdElement.send_keys('admin123'))

# driver.find_element(By.NAME, "username").send_keys("Admin")
# driver.find_element(By.NAME, "password").send_keys("admin123")
# driver.find_element(By.ID, "btnLogin").click()

    act_title = driver.title
    exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login test pass")
else:
    print("Login test fail")

#driver.close()

