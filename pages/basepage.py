from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def find_element(driver, locator, waiting_time=10):
    return WebDriverWait(driver, waiting_time).until(EC.visibility_of_element_located(locator),
                                                     message=f"Can't find element by locator {locator}")


def find_elements(driver, locator, waiting_time=10):
    return WebDriverWait(driver, waiting_time).until(EC.visibility_of_all_elements_located(locator),
                                                     message=f"Can't find elements by locator {locator}")


def is_element_visible(driver, locator, waiting_time=10):
    try:
        if WebDriverWait(driver, waiting_time).until(EC.visibility_of_element_located(locator),
                                                     message=f"Element by locator {locator} isn't visible"):
            return True
    except TimeoutException:
        return False


def input_text(driver, locator, text, waiting_time=10):
    find_element(driver, locator, waiting_time).click()
    find_element(driver, locator, waiting_time).clear()
    find_element(driver, locator, waiting_time).send_keys(text)
