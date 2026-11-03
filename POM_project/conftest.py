import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.page_load_strategy = "eager"
    
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()