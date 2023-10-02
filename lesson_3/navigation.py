from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.get("https://google.com/")
sleep(5)
driver.back()
sleep(3)
driver.forward()
sleep(3)
driver.refresh()
sleep(3)