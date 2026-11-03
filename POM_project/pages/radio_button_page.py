from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RadioButtonPage(BasePage):
    URL = "https://demoqa.com/radio-button"

    YES_LABEL = (By.XPATH, "//label[@for='yesRadio']")
    IMPRESSIVE_LABEL = (By.XPATH, "//label[@for='impressiveRadio']")
    NO_RADIO_INPUT = (By.ID, "noRadio")
    SUCCESS_TEXT = (By.CLASS_NAME, "text-success")


    ALL_LABELS = (By.XPATH, "//div[contains(@class, 'custom-radio')]/label")

    def open_page(self):
        self.open(self.URL)

    def select_yes(self):
        self.click(self.YES_LABEL)

    def select_impressive(self):
        self.click(self.IMPRESSIVE_LABEL)

    def is_no_option_disabled(self):
        return not self.find(self.NO_RADIO_INPUT).is_enabled()

    def get_selected_result_text(self):
        return self.get_text(self.SUCCESS_TEXT)

    def get_all_radio_labels_text(self):
        return self.get_elements_text(self.ALL_LABELS)