from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import pytest


@pytest.fixture(params=["google-chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "google-chrome":
        options = webdriver.ChromeOptions()
        service = Service(executable_path="/usr/local/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        service = Service(executable_path="/usr/local/bin/geckodriver")
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Invalid browser specified: {browser}")
    yield driver
    driver.quit()
