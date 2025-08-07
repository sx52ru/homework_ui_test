# тест оформления заказа

from utils.config import Config
from playwright.sync_api import Page, expect

# тестируем добавление товара в корзину
def test_store_add_to_cart(login_store):
    login_store.get_by_role("link", name="Phones", exact=True).click()
    login_store.get_by_role("link", name="Sony xperia z5", exact=True).click()
    login_store.get_by_role("link", name="Add to cart", exact=True).click()
    login_store.on("dialog", lambda dialog: dialog.accept())
    login_store.get_by_role("link", name="Cart", exact=True).click()
    assert login_store.get_by_text("Sony xperia z5", exact=True)

# тестируем оформление заказа
def test_store_place_order(login_store):
    login_store.get_by_role("link", name="Phones", exact=True).click()
    login_store.get_by_role("link", name="Sony xperia z5", exact=True).click()
    login_store.get_by_role("link", name="Add to cart", exact=True).click()
    login_store.on("dialog", lambda dialog: dialog.accept())
    login_store.get_by_role("link", name="Cart", exact=True).click()
    login_store.get_by_role("button", name="Place Order", exact=True).click()
    input_locator = login_store.locator("input[id='name']")
    input_locator.click()
    input_locator.type(Config.ORDER_NAME)
    input_locator = login_store.locator("input[id='country']")
    input_locator.click()
    input_locator.type(Config.ORDER_COUNTRY)
    input_locator = login_store.locator("input[id='city']")
    input_locator.click()
    input_locator.type(Config.ORDER_CITY)
    input_locator = login_store.locator("input[id='card']")
    input_locator.click()
    input_locator.type(Config.CREDIT_CARD)
    input_locator = login_store.locator("input[id='month']")
    input_locator.click()
    input_locator.type(Config.ORDER_MONTH)
    input_locator = login_store.locator("input[id='year']")
    input_locator.click()
    input_locator.type(Config.ORDER_YEAR)
    login_store.get_by_role("button", name="Purchase", exact=True).click()
    assert login_store.get_by_text("Card Number: " + Config.CREDIT_CARD, exact=True)
    assert login_store.get_by_text("Name: " + Config.ORDER_NAME, exact=True)
