import os
from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_optional = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}\\downloads"
}
chrome_optional.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_optional)
driver.get("https://the-internet.herokuapp.com/download")
sleep(3)
driver.find_elements("xpath", "//a")[1].click()
sleep(10)

