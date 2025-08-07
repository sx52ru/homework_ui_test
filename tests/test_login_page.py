# тест логина
from utils.config import Config
from playwright.sync_api import Page, expect

# тестируем открытие страницы магазина
def test_store_open_page(open_page):
    expect(open_page).to_have_title("STORE")

# тестируем авторизацию
def test_store_login(open_page):
    open_page.get_by_role("link", name="Log in").click()
    input_locator = open_page.locator("input[id='loginusername']")
    input_locator.click()
    input_locator.type(Config.USER_NAME)
    input_locator = open_page.locator("input[id='loginpassword']")
    input_locator.click()
    input_locator.type(Config.PASSWORD)
    open_page.get_by_role("button", name="Log in").click()
    assert open_page.get_by_text("Welcome admin", exact=True)
