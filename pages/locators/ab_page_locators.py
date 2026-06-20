from selenium.webdriver.common.by import By



class ABPageLocators:
    AB_TEST_PAGE_HEADER = (By.XPATH, "//h3[contains(text(), 'A/B Test Control')]")
    PAGE_CONTENT = (By.XPATH, "//div[@class = 'example']//p[contains(text(), 'Also know')]")

    