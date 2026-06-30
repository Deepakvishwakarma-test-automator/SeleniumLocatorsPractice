from selenium.webdriver.common.by import By

class Dropdown_locators():

    DROPDOWN_TITLE_PAGE = (By.XPATH, "//h3[contains(text(), 'Dropdown List')]")
    DROPDOWN_OPTION = (By.XPATH, "//select[@id= 'dropdown']")
    
