from pages.locators.landing_page_locators import LandingPage 

class LandingPage:
    def __init__(self,driver):
        self.driver = driver
    
    def get_header_text(self):
        header_element = self.driver.find_element(*LandingPage.HEADER_TEXT)
        return header_element.text
    
    def get_title(self):
        return self.driver.title    