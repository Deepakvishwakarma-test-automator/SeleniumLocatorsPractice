from pages.pages.checkbox_page import Select_Checkboxes
from pages.pages.landing_page import LandingPage


def test_check_box(driver):

#open checkbox page
    lp = LandingPage(driver)
    lp.click_checkbox_link()


    check = Select_Checkboxes(driver)
    check.select_checkbox(0)
    assert check.is_checkbox_selected(0)

    assert check.is_checkbox_selected(1)


    driver.back()
    assert "The Internet" in driver.title
    driver.forward()
    assert check.checkbox_title()






