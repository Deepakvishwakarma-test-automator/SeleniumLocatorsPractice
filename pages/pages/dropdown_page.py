from pages.locators.dropdown_page_locators import Dropdown_locators
from pages.base_setup_page import BaseSetupPage

class Dropdown_page():

    def __init__(self, driver):
        self.driver = driver 

    def title_dropdown_page(self):
        return self.driver.find_element(*Dropdown_locators.DROPDOWN_TITLE_PAGE)
    
    
    
