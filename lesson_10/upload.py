import os
from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_optional = webdriver.ChromeOptions()

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_optional)

driver.get("https://the-internet.herokuapp.com/upload")
driver.find_element("xpath", "//input[@type='file']").send_keys(f"{os.getcwd()}\\downloads\\some-file.txt")
sleep(3)
driver.find_element("xpath", "//input[@id='file-submit']").click()
sleep(5)
