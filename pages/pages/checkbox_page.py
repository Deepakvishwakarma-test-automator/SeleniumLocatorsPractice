
from pages.locators.checkbox_page_locators import Checkbox_page_locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Select_Checkboxes():
    def __init__(self, driver):
        self.driver = driver 
        self.wait = WebDriverWait(driver,10)

    def get_checkboxes(self):
        return self.driver.find_elements(*Checkbox_page_locators.CHECKBOX)

    def select_checkbox(self, index):
        checkboxes = self.get_checkboxes()[index]

        if not checkboxes.is_selected():
            checkboxes.click()

    def is_checkbox_selected(self, index):
        return self.get_checkboxes()[index].is_selected()

    def checkbox_title(self):
        return self.wait.until(EC.visibility_of_element_located(Checkbox_page_locators.CHECKBOXES_PAGE_TITLE)).is_displayed