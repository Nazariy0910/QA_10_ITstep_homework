from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DynamicPropertiesPage(BasePage):
    URL = "https://demoqa.com/dynamic-properties"

    ENABLE_AFTER_BUTTON = (By.ID, "enableAfter")
    COLOR_CHANGE_BUTTON = (By.ID, "colorChange")
    VISIBLE_AFTER_BUTTON = (By.ID, "visibleAfter")

    def open_page(self):
        self.open(self.URL)

    def is_enable_after_button_enabled(self):
        return self.find(self.ENABLE_AFTER_BUTTON).is_enabled()

    def wait_until_button_enabled(self):
        return self.wait_clickable(self.ENABLE_AFTER_BUTTON, timeout=7)

    def is_color_changed(self):
        return self.has_class(
            self.COLOR_CHANGE_BUTTON, "text-danger", timeout=7
        )

    def is_visible_after_button_shown(self):
        return self.is_visible(self.VISIBLE_AFTER_BUTTON, timeout=7)