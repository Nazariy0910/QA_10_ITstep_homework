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
    driver.get("https://demoqa.com/alerts")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    prompt_button = wait.until(
        EC.element_to_be_clickable((By.ID, "promtButton"))
    )
    prompt_button.click()

    alert = wait.until(EC.alert_is_present())

    my_text = "Nazarii"
    alert.send_keys(my_text)

    alert.accept()

    result_element = wait.until(
        EC.presence_of_element_located((By.ID, "promptResult"))
    )
    result_text = result_element.text
    print(f"Text on the page: {result_text}")

    assert (
        my_text in result_text
    ), f"Error! Expected'{my_text}' у тексті '{result_text}'"
    print("✅The test has been passed successfully! The text matches.")

finally:
    driver.quit()