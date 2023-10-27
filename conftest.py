from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import pytest


@pytest.fixture(params=["google-chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "google-chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Invalid browser specified: {browser}")
    yield driver
    driver.quit()
