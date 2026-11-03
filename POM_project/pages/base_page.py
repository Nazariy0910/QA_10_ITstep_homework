from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)
        self.remove_ads()

    def remove_ads(self):
        self.driver.execute_script(
            "document.querySelectorAll('#fixedban, footer').forEach(el => el.remove());"
        )

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def is_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0

    def is_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def type_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        element.click()

    def has_class(self, locator, class_name, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element_attribute(
                    locator, "class", class_name
                )
            )
            return True
        except TimeoutException:
            return False

    def get_current_url(self):
        return self.driver.current_url

    # --- Завдання 4: Нові універсальні методи ---
    def get_title(self):
        """Чекає, поки заголовок сторінки стане непорожнім, та повертає його"""
        WebDriverWait(self.driver, 10).until(lambda d: d.title != "")
        return self.driver.title

    def wait_url_contains(self, part):
        self.wait.until(EC.url_contains(part))

    def get_elements_text(self, locator, timeout=20):
        """Повертає список текстів усіх знайдених елементів"""
        elements = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return [element.text for element in elements]