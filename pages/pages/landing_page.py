from pages.locators.landing_page_locators import LandingPageLocators

class LandingPage:
    def __init__(self,driver):
        self.driver = driver
    
    def get_sub_header_text(self):
        sub_header_element = self.driver.find_element(*LandingPageLocators.SUBHEADER_TEXT)
        return sub_header_element.text
    
    def get_title(self):
        return self.driver.title    