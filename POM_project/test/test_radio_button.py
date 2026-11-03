from pages.radio_button_page import RadioButtonPage


def test_radio_button_yes(driver):
    page = RadioButtonPage(driver)
    page.open_page()
    page.select_yes()
    assert page.get_selected_result_text() == "Yes"


def test_radio_button_impressive(driver):
    page = RadioButtonPage(driver)
    page.open_page()
    page.select_impressive()
    assert page.get_selected_result_text() == "Impressive"


def test_radio_button_no_disabled(driver):
    page = RadioButtonPage(driver)
    page.open_page()
    assert (
        page.is_no_option_disabled()
    ), "Опція 'No' повинна бути заблокована (disabled)"