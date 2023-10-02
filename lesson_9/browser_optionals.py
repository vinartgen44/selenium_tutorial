from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_optional = webdriver.ChromeOptions()
# chrome_optional.add_argument('--headless')
chrome_optional.add_argument('--incognito')
chrome_optional.add_argument('--ignore-certificate-errors')
chrome_optional.add_argument('--window-size=1920,1080')
chrome_optional.add_argument('--disable-cache')
chrome_optional.page_load_strategy = 'eager'
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_optional)
driver.get("https://whatismyipaddress.com/")
# driver.get("https://expired.badssl.com/")
print(driver.title)
sleep(3)
