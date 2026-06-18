import pytest
from pages.pages.landing_page import LandingPage


def test_landing_page(driver):
    lp = LandingPage(driver)
    assert lp.get_title() == "Welcome to the Internet"
    #assert lp.get_header_text() == "Available Examples"

