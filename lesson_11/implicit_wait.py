from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_optional = webdriver.ChromeOptions()
chrome_optional.add_argument("--incognito")
chrome_optional.add_argument("--headless")
chrome_optional.page_load_strategy = "eager"
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_optional)
driver.implicitly_wait(10)

VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")

driver.get("https://demoqa.com/dynamic-properties")

driver.find_element(*VISIBLE_AFTER_BUTTON).click()
