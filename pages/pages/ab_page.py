from pages.locators.ab_page_locators import ABPageLocators
from pages.locators.landing_page_locators import LandingPageLocators


class ABPage:
    def __init__(self, driver):
        self.driver = driver


    def click_link(self):
        link_element = self.driver.find_element(*LandingPageLocators.AB_TEST_PAGE_LINK)
        link_element.click()
    

    def get_sub_header_text(self):
        sub_header_element = self.driver.find_element(*ABPageLocators.SUBHEADER_TEXT)
        return sub_header_element.text

    def get_title(self):
        return self.driver.title
    
    def get_page_content(self):
        page_content_element = self.driver.find_element(*ABPageLocators.PAGE_CONTENT)
        return page_content_element.text    
    
    