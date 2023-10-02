from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.get("https://www.wikipedia.org/")
url = driver.current_url
title = driver.title

assert url == "https://www.wikipedia.org/", "The url does not match"
assert title == "Wikipedia", "The title does not match"
