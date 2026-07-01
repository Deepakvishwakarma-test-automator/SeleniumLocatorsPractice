import pytest
from pages.pages.dropdown_page import DropdownPage
from pages.pages.landing_page import LandingPage


class TestDropdown:

    def test_select_option_by_visible_text(self, driver):

        lp = LandingPage(driver)
        lp.click_dropdown_link()

        dropdown_page = DropdownPage(driver)

        dropdown_page.select_by_text("Option 1")

        assert dropdown_page.get_selected_option() == "Option 1"