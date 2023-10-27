from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import pytest


@pytest.fixture(params=["google-chrome", "firefox"])
def driver(request):
    browser = request.param
    options = Options()
    options.add_argument("--headless")
    if browser == "google-chrome":
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Invalid browser specified: {browser}")
    yield driver
    driver.quit()
