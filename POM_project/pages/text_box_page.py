from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TextBoxPage(BasePage):
    URL = "https://demoqa.com/text-box"

    FULL_NAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_INPUT = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")

    OUTPUT_NAME = (By.XPATH, "//div[@id='output']//p[@id='name']")
    OUTPUT_EMAIL = (By.XPATH, "//div[@id='output']//p[@id='email']")
    OUTPUT_CURRENT_ADDRESS = (
        By.XPATH,
        "//div[@id='output']//p[@id='currentAddress']",
    )
    OUTPUT_PERMANENT_ADDRESS = (
        By.XPATH,
        "//div[@id='output']//p[@id='permanentAddress']",
    )

    def open_page(self):
        self.open(self.URL)

    def fill_form(
        self,
        full_name="",
        email="",
        current_address="",
        permanent_address="",
    ):
        self.type_text(self.FULL_NAME_INPUT, full_name)
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.CURRENT_ADDRESS_INPUT, current_address)
        self.type_text(self.PERMANENT_ADDRESS_INPUT, permanent_address)

    def submit(self):
        self.click(self.SUBMIT_BUTTON)

    def get_output_name(self):
        return self.get_text(self.OUTPUT_NAME)

    def get_output_email(self):
        return self.get_text(self.OUTPUT_EMAIL)

    def get_output_current_address(self):
        return self.get_text(self.OUTPUT_CURRENT_ADDRESS)

    def get_output_permanent_address(self):
        return self.get_text(self.OUTPUT_PERMANENT_ADDRESS)

    def is_email_marked_invalid(self):
        return self.has_class(self.EMAIL_INPUT, "field-error")

    def is_output_shown(self):
        return self.is_present(self.OUTPUT_NAME)