from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    wait = WebDriverWait(driver, 10)

    driver.get("https://demoqa.com/alerts")
    driver.maximize_window()

    confirm_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "confirmButton"))
    )
    confirm_btn.click()

    alert = wait.until(EC.alert_is_present())
    alert.dismiss()

    confirm_result = wait.until(
        EC.presence_of_element_located((By.ID, "confirmResult"))
    )
    result_text_1 = confirm_result.text
    print(f"Result after Cancel: {result_text_1}")
    assert (
        "Cancel" in result_text_1
    ), f"We were expecting Cancel, but we got: {result_text_1}"

    confirm_btn.click()

    alert = wait.until(EC.alert_is_present())
    alert.accept()

    result_text_2 = confirm_result.text
    print(f"Result after pressing OK: {result_text_2}")
    assert (
        "Ok" in result_text_2
    ), f"We were expecting Ok, but what we got was: {result_text_2}"

    driver.get("https://demoqa.com/browser-windows")

    original_window = driver.current_window_handle

    assert (
        len(driver.window_handles) == 1
    ), "Only one tab should be open!"

    tab_btn = wait.until(EC.element_to_be_clickable((By.ID, "tabButton")))
    tab_btn.click()

    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    heading_element = wait.until(
        EC.presence_of_element_located((By.ID, "sampleHeading"))
    )
    sample_text = heading_element.text
    print(f"Text in new tab: {sample_text}")

    assert (
        sample_text == "This is a sample page"
    ), f"Expected 'This is a sample page', but received: {sample_text}"

    driver.close()
    driver.switch_to.window(original_window)

    print("✅ Everything is working now")

finally:
    driver.quit()