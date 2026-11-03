from pages.text_box_page import TextBoxPage


def test_email_without_at(driver):
    page = TextBoxPage(driver)
    page.open_page()
    page.fill_form(full_name="Ivan Tester", email="ivan.tester.com")
    page.submit()
    assert (
        page.is_email_marked_invalid()
    ), "Email без @ повинен підсвічуватися червоним"
    assert (
        not page.is_output_shown()
    ), "Блок результату не повинен з'являтися при невалідному email"


def test_email_without_domain(driver):
    page = TextBoxPage(driver)
    page.open_page()
    page.fill_form(full_name="Ivan Tester", email="ivan@")
    page.submit()
    assert (
        page.is_email_marked_invalid()
    ), "Email без домену повинен підсвічуватися червоним"
    assert (
        not page.is_output_shown()
    ), "Блок результату не повинен з'являтися при невалідному email"


def test_email_with_space(driver):
    page = TextBoxPage(driver)
    page.open_page()
    page.fill_form(full_name="Ivan Tester", email="ivan @test.com")
    page.submit()
    assert (
        page.is_email_marked_invalid()
    ), "Email з пробілом повинен підсвічуватися червоним"
    assert (
        not page.is_output_shown()
    ), "Блок результату не повинен з'являтися при невалідному email"


def test_email_without_tld(driver):
    page = TextBoxPage(driver)
    page.open_page()
    page.fill_form(full_name="Ivan Tester", email="ivan@test")
    page.submit()
    assert (
        page.is_email_marked_invalid()
    ), "Email без доменної зони повинен підсвічуватися червоним на demoqa"
    assert (
        not page.is_output_shown()
    ), "Блок результату не повинен з'являтися при невалідному email"


def test_empty_form_submit(driver):
    page = TextBoxPage(driver)
    page.open_page()
    page.submit()
    assert (
        not page.is_email_marked_invalid()
    ), "Email необов'язковий, підсвічування бути не повинно"
    assert (
        not page.is_output_shown()
    ), "Порожня форма не повинна виводити блок результату"