import pytest
from pages.pages.landing_page import LandingPage


def test_landing_page_title(driver):
    lp = LandingPage(driver)
    assert lp.get_title() == "The Internet"
    print(lp.get_title())
    

def test_landing_page_sub_header_text(driver):
    lp = LandingPage(driver)
    sub_header_text = lp.get_sub_header_text()
    assert sub_header_text == "Available Examples"
    print(sub_header_text)
