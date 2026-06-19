import pytest
from selenium import webdriver
from util.config_reader import ConfigReader

config = ConfigReader()
Baseurl = config.get("Default", "BaseURL")
Browser = config.get("Default", "Browser")

@pytest.fixture(scope="function")
def driver():
    if Browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif Browser.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {Browser}")

    driver.maximize_window()
    driver.get(Baseurl)
    yield driver
    driver.quit()
