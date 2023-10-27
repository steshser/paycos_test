from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import pytest


@pytest.fixture(params=["google-chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "google-chrome":
        chrome_path = "/usr/bin/google-chrome"
        chrome_driver_path = "/usr/local/bin/chromedriver"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = chrome_path
        driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Invalid browser specified: {browser}")
    yield driver
    driver.quit()
