from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
try:
    driver.get("https://demoqa.com/nestedframes")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1")))

    parent_body = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    parent_text = parent_body.text
    print(f"Text within the frame: {parent_text}")

    wait.until(
        EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe"))
    )

    child_body = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    child_text = child_body.text
    print(f"Text within the frame: {child_text}")

    assert (
        "Parent frame" in parent_text
    ), f"Error! We expected “Parent frame”, but received: {parent_text}"
    assert (
        "Child Iframe" in child_text
    ), f"Error! We expected “Child Iframe”, but received: {child_text}"
    print("✅Both assertions passed successfully!")

    driver.switch_to.default_content()

finally:
    driver.quit()