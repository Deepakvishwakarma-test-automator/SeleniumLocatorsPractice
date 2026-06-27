from selenium.webdriver.common.by import By


class ContextPage_locators():
    HEADER_TEXT = (By.XPATH, "//h3[normalize-space() = 'Context Menu']")
    CONTEXT_BOX = (By.XPATH, "//div[@id='hot-spot']")

