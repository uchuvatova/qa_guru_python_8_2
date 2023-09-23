import pytest
from selene import browser

GOOGLE = 'https://google.ru'
@pytest.fixture(scope='function')
def open_browser():
    browser.open(GOOGLE)
    browser.driver.maximize_window()
    yield
    browser.quit()
