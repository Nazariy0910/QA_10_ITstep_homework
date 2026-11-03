
# pages/forms_page.py
from pages.base_page import BasePage
from pages.practice_form_page import PracticeFormPage
from selenium.webdriver.common.by import By


class FormsPage(BasePage):
    PRACTICE_FORM_ITEM = (By.XPATH, '//span[text()="Practice Form"]')

    def go_to_practice_form(self):
        self.click(self.PRACTICE_FORM_ITEM)
        self.wait_url_contains("automation-practice-form")
        self.remove_ads()
        return PracticeFormPage(self.driver)    