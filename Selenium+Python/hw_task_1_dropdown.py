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

    driver.get("https://demoqa.com/select-menu")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)
    select_element = wait.until(
        EC.presence_of_element_located((By.ID, "oldSelectMenu"))
    )

    select = Select(select_element)

    select.select_by_index(1) 
    text_1 = select.first_selected_option.text
    print(f"Current selection (Method 1): {text_1}")

    select.select_by_value("3") 
    text_2 = select.first_selected_option.text
    print(f"Current selection (Method 2): {text_2}")

    select.select_by_visible_text("Magenta") 
    text_3 = select.first_selected_option.text
    print(f"Current selection (Method 3): {text_3}")

    assert text_3 == 'Magenta', f"We were expecting Magenta, but the following was selected:{text_3}"
    print("✅ The test has been passed successfully! The final choice is Magenta.")

finally:
    driver.quit()