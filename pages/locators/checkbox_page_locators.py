from selenium.webdriver.common.by import By


class Checkbox_page_locators():
    CHECKBOXES_PAGE_TITLE = (By.XPATH, "//div[@class='example']/h3[contains(text(), 'Checkbox')]")
    CHECKBOX = (By.XPATH, "//form[@id = 'checkboxes']/input[@type='checkbox']")

