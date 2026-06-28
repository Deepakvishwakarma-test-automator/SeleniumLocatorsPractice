from pages.pages.checkbox_page import Select_Checkboxes
from pages.pages.landing_page import LandingPage


def test_check_box(driver):

    lp = LandingPage(driver)
    lp.click_checkbox_link

