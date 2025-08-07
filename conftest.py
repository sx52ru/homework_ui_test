# фикстуры

from utils.config import Config
import pytest
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright

# фикстура создает контекст
@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

# фикстура открывает браузер
@pytest.fixture(scope="session")
def open_page(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000, timeout=10000)
    page = browser.new_page()
    page.goto(Config.BASE_URL)
    yield page
    browser.close()

# фикстура открывает браузер и авторизуется
@pytest.fixture(scope="session")
def login_store(open_page):
    open_page.get_by_role("link", name="Log in").click()
    input_locator = open_page.locator("input[id='loginusername']")
    input_locator.click()
    input_locator.type(Config.USER_NAME)
    input_locator = open_page.locator("input[id='loginpassword']")
    input_locator.click()
    input_locator.type(Config.PASSWORD)
    open_page.get_by_role("button", name="Log in").click()
    yield open_page
    open_page.close()