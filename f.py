from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

def wait_for_element_click(locator):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator)).click()

def login_to_facebook(email, password):
    driver.get("https://www.facebook.com/")
    wait_for_element_click((By.ID, "email")).send_keys(email)
    wait_for_element_click((By.ID, "pass")).send_keys(password)
    wait_for_element_click((By.NAME, "login"))

def report_account(account_url):
    driver.get(account_url)
    wait_for_element_click((By.XPATH, '//div[contains(@aria-label, "More options")]'))
    try:
        wait_for_element_click((By.XPATH, '//span[text()="Find support or report profile"]'))
    except NoSuchElementException:
        # Handle potential alternative menus
        print("Alternative menu structure encountered. Adapting...")  # Add specific logic here

    wait_for_element_click((By.LINK_TEXT, "Report profile"))
    wait_for_element_click((By.XPATH, '//span[text()="Me"]'))  # Select a reason for reporting
    wait_for_element_click((By.XPATH, '//div[text()="Submit"]'))
    wait_for_element_click((By.XPATH, '//button[text()="Next"]'))
    wait_for_element_click((By.XPATH, '//button[text()="Done"]'))

try:
    login_to_facebook("your_email@example.com", "your_password")
    account_to_report = "https://www.facebook.com/profile.php?id=100089108025261"  # Replace with actual URL
    report_account(account_to_report)
except (TimeoutException, NoSuchElementException) as e:
    print("An error occurred:", e)
finally:
    driver.quit()
