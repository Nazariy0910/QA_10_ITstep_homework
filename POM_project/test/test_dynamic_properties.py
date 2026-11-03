from pages.dynamic_properties_page import DynamicPropertiesPage


def test_enable_after_button(driver):
    page = DynamicPropertiesPage(driver)
    page.open_page()
    assert (
        not page.is_enable_after_button_enabled()
    ), "Кнопка має бути спочатку заблокована"
    page.wait_until_button_enabled()
    assert (
        page.is_enable_after_button_enabled()
    ), "Кнопка має стати активною через 5 секунд"


def test_color_change_button(driver):
    page = DynamicPropertiesPage(driver)
    page.open_page()
    assert (
        page.is_color_changed()
    ), "Клас text-danger повинен з'явитися через 5 секунд"


def test_visible_after_button(driver):
    page = DynamicPropertiesPage(driver)
    page.open_page()
    assert (
        page.is_visible_after_button_shown()
    ), "Кнопка повинна з'явитися через 5 секунд"