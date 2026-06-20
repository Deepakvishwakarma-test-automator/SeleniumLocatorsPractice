
from pages.pages.ab_page import ABPage

def test_ab_page_title(driver):

    ab_page = ABPage(driver)

    print(ab_page.get_title())

    ab_page.click_link()

    content = ab_page.get_page_content()

    assert "Also know" in content

    print(content)

