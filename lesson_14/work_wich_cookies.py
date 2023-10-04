from time import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

start = time()
user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
              "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36")

chrome_optional = webdriver.ChromeOptions()
chrome_optional.add_argument("--window-size=1920,1080")
chrome_optional.add_argument("--disable-blink-features=AutomationControlled")
chrome_optional.add_argument(f"--user-agent={user_agent}")
chrome_optional.add_argument("--incognito")
chrome_optional.add_argument("--headless")
chrome_optional.page_load_strategy = "eager"

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_optional)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/ru/ru/login")
# print(driver.get_cookie("country_code"))
driver.add_cookie({
    "name": "Example",
    "value": "Cuckoo"
})
print(driver.get_cookie("Example"))
