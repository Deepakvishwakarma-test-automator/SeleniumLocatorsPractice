
from pages.locators.checkbox_page_locators import Checkbox_page_locators
from selenium.webdriver.support.ui import WebDriverWait



class Select_Checkboxes():
    def __init__(self, driver):
        self.driver = driver 
        self.waitait = WebDriverWait(driver,10)

    def get_checkboxes(self):
        return self.driver.find_elements(*Checkbox_page_locators.CHECKBOX)

    def select_checkbox(self, index):
        checkboxes = self.get_checkboxes()[index]

        if not checkboxes.is_selected():
            checkboxes.click()

    def is_checkbox_selected(self, index):
        return self.get_checkboxes()[index].is_selected()
