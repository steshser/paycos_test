from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
import pytest


@pytest.fixture(params=["google-chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "google-chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Invalid browser specified: {browser}")
    yield driver
    driver.quit()
