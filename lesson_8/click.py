from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.freeconferencecall.com/ru/ru")
login_button = driver.find_element("xpath", "//a[@id='login-desktop']")
login_button.click()
email = driver.find_element("xpath", "//input[@type='email']")
password = driver.find_element("xpath", "//input[@type='password']")
email.send_keys("example@mail.ru")
password.send_keys("exampl")
sleep(3)
