from pages.base_setup_page import BaseSetupPage
from pages.locators.dropdown_page_locators import DropdownLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import Select

class DropdownPage(BaseSetupPage):

    def __init__(self, driver):
        super().__init__(driver)

    def _dropdown(self):
        element = self.wait.until(
            EC.element_to_be_clickable(
                DropdownLocators.DROPDOWN_OPTION
            )
        )
        return Select(element)

    def select_by_text(self, text: str):
        self._dropdown().select_by_visible_text(text)

    def select_by_index(self, index: int):
        self._dropdown().select_by_index(index)

    def select_by_value(self, value: str):
        self._dropdown().select_by_value(value)

    def get_selected_option(self) -> str:
        return self._dropdown().first_selected_option.text
    
    