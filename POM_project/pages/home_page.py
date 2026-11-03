from pages.base_page import BasePage
from pages.elements_page import ElementsPage
from pages.forms_page import FormsPage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    URL = "https://demoqa.com/"

    ELEMENTS_CARD = (By.XPATH, '//h5[text()="Elements"]')
    FORMS_CARD = (By.XPATH, '//h5[text()="Forms"]')

    def open_page(self):
        self.open(self.URL)
        return self

    def go_to_elements(self):
        self.click(self.ELEMENTS_CARD)
        self.wait_url_contains("elements")
        return ElementsPage(self.driver)

    def go_to_forms(self):
        self.click(self.FORMS_CARD)
        self.wait_url_contains("forms")
        return FormsPage(self.driver)