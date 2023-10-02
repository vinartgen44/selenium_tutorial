from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.get("https://www.freeconferencecall.com/ru/ru/login")

driver.find_element("id", "loginformsubmit").click()
sleep(3)
