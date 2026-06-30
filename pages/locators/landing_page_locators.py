from selenium.webdriver.common.by import By

class LandingPageLocators:
    SUBHEADER_TEXT = (By.XPATH, "//h2[contains(text(), 'Available Examples')]")
    AB_TEST_PAGE_LINK = (By.XPATH, "//a[contains(text(), 'A/B Testing')]")
    ADD_REMOVE_ELEMENTS_PAGE_LINK = (By.XPATH, "*//a[contains(text(), 'Add/Remove Elements')]")
    BASIC_AUTH_PAGE_LINK = (By.XPATH, "//a[text() = 'Basic Auth']")
    CONTEXT_MENU_PAGE_LINK = (By.XPATH, "//a[contains(text(), 'Context Menu')]")
    CHECK_BOXE_PAGE = (By.XPATH, "//a[contains(normalize-space(), 'Checkboxes')]")
    DROPDOWN_PAGE = (By.XPATH, '//a[contains(text(), 'Dropdown')]')

    
    