**Selenium-WebDrive-Python-Example**	

This repository contains the base setup of Selenium Webdriver, Using python to identify elements page object.

     Locate
     Find element, elements
     Implicit, Explicit wait
     Handles Brokenlinks,  Checkbox,  Dropdow list
     Alert Popup(driver.switch_to_alert) 
     Frames/Iframes: switch_to.frame(name of the frame)
     Browser windows: switch_to.window(WindowID)
     File Down, Upload
     Drag/Drop, RightClick, Scrolling, Slide
     Date Picker
     Capture Screenshot, TabWindow
     Data Driven DB
     
Requirements
Setup & configure WebDriver in Pycharm
---------------------------------------
Pre-requisites:
----------
  Selenium 4.12.0
  
  Python 3.9
  
  Pychamp

1) Download browser specific drivers using below links....	

    Chrome:	https://chromedriver.chromium.org/downloads
    
    Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
    
    Firefox:	https://github.com/mozilla/geckodriver/releases	
    
    Once you donwloaded, extract .zip files then you will see .exe files ( they are drivers)

2) setup selenium webdriver
   
	Appraoch#

    pip install selenium
   
	Appraoch#2:

		or through Pycharm project settings...

**Test Cases**

	1) Open Web Browser(Chrome/firefox/Edge).
	2) Open URL  https://opensource-demo.orangehrmlive.com/
	3) Enter username  (Admin).
	4) Enter password  (admin123).   
	5) Click on Login.
	6) Capture title of the home page.(Actual title) 
	7) Verify title of the page: OrangeHRM    (Expected)
	8) close browser

**Test Excution**

    Open Pycharm 
    Open Project > Run on test    



