import pytest
from selene import browser



@pytest.fixture(scope="function")
def browser_open_page():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.open("https://demoqa.com/automation-practice-form")
    yield
    browser.quit()
