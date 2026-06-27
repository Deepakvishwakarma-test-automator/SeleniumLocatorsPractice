import pytest
from pages.pages.landing_page import LandingPage
from pages.pages.context_page import ContextPage


class TestContextMenu:

    def test_context_menu(self, driver):
        #object for landing pg
        landing_page = LandingPage(driver)
        #navigate to context page 
        landing_page.click_context_menu_link()
        #object for context page 
        context_page = ContextPage(driver)
        assert context_page.get_header_text() == "Context Menu"
        context_page.right_click_context_box()
        #alert_text = context_page.get_alert_text()
        #assert alert_text == "You selected a context menu"
        context_page.accept_alert()
        driver.wait(5)

