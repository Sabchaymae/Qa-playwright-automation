from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from playwright.sync_api import expect

def test_add_product_to_cart(login_page):
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(login_page.page)

    products_page.add_backpack_to_cart()

    cart_page = CartPage(login_page.page)

    expect(cart_page.cart_badge).to_have_text("1")

def test_backpack_is_present_in_cart(login_page):
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(login_page.page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(login_page.page)
    cart_page.open_cart()

    expect(cart_page.backpack_item).to_have_text("Sauce Labs Backpack")

def test_backpack_quantity_is_one(login_page):
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(login_page.page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(login_page.page)
    cart_page.open_cart()

    expect(cart_page.backpack_quantity).to_have_text("1")

def test_remove_backpack_from_cart(login_page):
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(login_page.page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(login_page.page)
    cart_page.open_cart()

    cart_page.remove_backpack_button.click()

    expect(cart_page.backpack_item).to_have_count(0)
    expect(cart_page.cart_badge).to_have_count(0)

def test_backpack_price_is_correct(login_page):
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(login_page.page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(login_page.page)
    cart_page.open_cart()

    expect(cart_page.backpack_price).to_have_text("$29.99")

def test_backpack_quantity_in_cart_is_one(login_page):
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(login_page.page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(login_page.page)
    cart_page.open_cart()

    expect(cart_page.backpack_quantity).to_have_text("1")

def test_cart_badge_is_two(login_page):
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(login_page.page)

    products_page.add_backpack_to_cart()
    products_page.add_bike_light_to_cart()

    cart_page = CartPage(login_page.page)

    expect(cart_page.cart_badge).to_have_text("2")