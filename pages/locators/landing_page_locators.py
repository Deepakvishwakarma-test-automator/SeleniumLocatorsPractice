from selenium.webdriver.common.by import By

class LandingPage:
    HEADER_TEXT = (By.XPATH, "//h2[contains(text(), 'Available Examples')]")
    