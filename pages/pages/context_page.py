from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_setup_page import BaseSetupPage
from pages.locators.context_page_locators import ContextPage_locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContextPage(BaseSetupPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_header_text(self):
        return self.get_element_text(ContextPage_locators.HEADER_TEXT)
    
    def right_click_context_box(self):
        try:
            context_box = self.get_element_text(ContextPage_locators.CONTEXT_BOX)
            actionchains = ActionChains(self.driver)
            actionchains.context_click(context_box).perform()

        except Exception as e:
            print(f"Right click failed: {e}")
            raise
                

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text

    
    def accept_alert(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def send_text_to_alert(self, text):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
