from selenium.webdriver.common.by import By
from pages.locators.landing_page_locators import LandingPageLocators    


class AddRemoveElementsLocators():
        HEADER_TEXT = (By.XPATH, "//h3[contains(text(), 'Add/Remove Elements')]")
        ADD_ELEMENT_BUTTON = (By.XPATH, "//button[contains(text(), 'Add Element')]")
        DELETE_BUTTON = (By.XPATH, "//button[@class = 'added-manually']")
        

