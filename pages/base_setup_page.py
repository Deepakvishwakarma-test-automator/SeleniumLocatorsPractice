from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 

class BaseSetupPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)   

    def click_element(self, Locator):
        element = self.wait.until(lambda driver: driver.find_element(*Locator))
        element.click()


    def get_element_text(self, Locator):
        element = self.wait.until(lambda driver: driver.find_element(*Locator))
        return element.text 
    
    def get_title(self):
        return self.driver.title
    

    def get_current_url(self):
        return self.driver.current_url
    

    def navigate_to_url(self, url):
        self.driver.get(url)


    
