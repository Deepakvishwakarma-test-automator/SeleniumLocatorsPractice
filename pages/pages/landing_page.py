from pages.locators.landing_page_locators import LandingPageLocators

class LandingPage:
    def __init__(self,driver):
        self.driver = driver
    
    def get_sub_header_text(self):
        sub_header_element = self.driver.find_element(*LandingPageLocators.SUBHEADER_TEXT)
        return sub_header_element.text
    
    def get_title(self):
        return self.driver.title    
    

    def click_add_remove_elements_link(self):
        add_remove_link = self.driver.find_element(*LandingPageLocators.ADD_REMOVE_ELEMENTS_PAGE_LINK)
        add_remove_link.click()
        
    def click_context_menu_link(self):
        context_menu_link = self.driver.find_element(*LandingPageLocators.CONTEXT_MENU_PAGE_LINK)
        context_menu_link.click()
        