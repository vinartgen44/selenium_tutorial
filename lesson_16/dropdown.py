from pprint import pprint
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
              "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36")

chrome_optional = webdriver.ChromeOptions()
chrome_optional.add_argument("--window-size=1920,1080")
chrome_optional.add_argument("--disable-blink-features=AutomationControlled")
chrome_optional.add_argument(f"--user-agent={user_agent}")
# chrome_optional.add_argument("--incognito")
# chrome_optional.add_argument("--headless")
# chrome_optional.page_load_strategy = "eager"

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_optional)
wait = WebDriverWait(driver, 10, poll_frequency=1)

TEXT_FIELD = ("xpath", "//input[@id='target']")

SELECT_LOCATOR = ("xpath", "(//input[@type='text'])[2]")

driver.get("https://demoqa.com/select-menu")
driver.find_element(*SELECT_LOCATOR).send_keys("Prof.")
driver.find_element(*SELECT_LOCATOR).send_keys(Keys.ENTER)
sleep(5)
