from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.locators.landing_page_locators import LandingPageLocators
from pages.locators.add_remove_elements_locators import AddRemoveElementsLocators


class AddRemoveElementsPage:
        def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)


     #   def get_header_text(self):
     #       header_element = self.driver.find_element(*AddRemoveElementsLocators.HEADER_TEXT)
      #      return header_element.text


        def click_add_element_button(self):
             add_element_button = self.wait.until(lambda driver: driver.find_element(*AddRemoveElementsLocators.ADD_ELEMENT_BUTTON))
             add_element_button.click()


        def click_delete_button(self):
            delete_button = self.wait.until(lambda driver: driver.find_element(*AddRemoveElementsLocators.DELETE_BUTTON))
            delete_button.click()

        def is_delete_button_present(self):
            try:
                self.driver.find_element(*AddRemoveElementsLocators.DELETE_BUTTON)
                return True
            except:
                return False
            

        def main_page(self):
             self.driver.back()
             return(title := self.driver.title)
        
        