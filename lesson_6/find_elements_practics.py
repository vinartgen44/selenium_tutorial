from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://hyperskill.org/tracks")

driver.find_elements("class name", "nav-link")[2].click()
sleep(3)