import pytest
from pages.pages.landing_page import LandingPage
from pages.pages.add_remove_el_page import AddRemoveElementsPage



def test_add_remove_page(driver):
    a_r_page_nav = LandingPage(driver).click_add_remove_elements_link()
    add_remove_page = AddRemoveElementsPage(driver)
    add_remove_page.click_add_element_button()
    assert add_remove_page.is_delete_button_present() == True
    add_remove_page.click_delete_button()
    assert add_remove_page.is_delete_button_present() == False
    

    




9