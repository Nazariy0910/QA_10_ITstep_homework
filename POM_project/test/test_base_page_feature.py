from pages.home_page import HomePage
from pages.radio_button_page import RadioButtonPage


def test_get_title_demoqa(driver):
    page = HomePage(driver)
    page.open_page()
    actual_title = page.get_title()
    assert (
        "DEMOQA" in actual_title.upper() or "DEMOSITE" in actual_title.upper()
    ), f"Заголовок повинен містити DEMOQA або DEMOSITE, але отримано: '{actual_title}'"


def test_wait_url_contains_navigation(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    elements_page = home_page.go_to_elements()
    text_box_page = elements_page.go_to_text_box()
    assert "text-box" in text_box_page.get_current_url()


def test_get_elements_text_radio_labels(driver):
    page = RadioButtonPage(driver)
    page.open_page()
    labels = page.get_all_radio_labels_text()
    assert labels == [
        "Yes",
        "Impressive",
        "No",
    ], f"Очікували ['Yes', 'Impressive', 'No'], але отримали {labels}"