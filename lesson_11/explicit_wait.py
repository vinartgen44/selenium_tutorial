from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from lesson_11.locators import REMOVE_BUTTON, ENABLE_BUTTON, INPUT_DISABLE, ENABLE_AFTER_BUTTON

chrome_optional = webdriver.ChromeOptions()
chrome_optional.add_argument("--window-size=1920,1080")
chrome_optional.add_argument("--incognito")
chrome_optional.add_argument("--headless")
chrome_optional.page_load_strategy = "eager"
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_optional)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://demoqa.com/dynamic-properties")
wait.until(EC.element_to_be_clickable(ENABLE_AFTER_BUTTON)).click()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")
driver.find_element(*REMOVE_BUTTON).click()
wait.until(EC.invisibility_of_element(REMOVE_BUTTON))
driver.find_element(*ENABLE_BUTTON).click()
wait.until(EC.element_to_be_clickable(INPUT_DISABLE)).send_keys("Hello")
wait.until(EC.text_to_be_present_in_element_value(INPUT_DISABLE, "Hello"))
