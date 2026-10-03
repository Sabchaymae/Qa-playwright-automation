from playwright.sync_api import expect

from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_access_checkout_from_cart(login_page):
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(login_page.page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(login_page.page)
    cart_page.open_cart()

    checkout_page = CheckoutPage(login_page.page)
    checkout_page.click_checkout()

    expect(checkout_page.checkout_title).to_have_text(
        "Checkout: Your Information"
    )


def test_checkout_empty_fields(login_page):
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(login_page.page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(login_page.page)
    cart_page.open_cart()

    checkout_page = CheckoutPage(login_page.page)
    checkout_page.click_checkout()

    checkout_page.continue_checkout()

    expect(checkout_page.error_message).to_have_text(
        "Error: First Name is required"
    )


def test_checkout_missing_first_name(login_page):
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(login_page.page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(login_page.page)
    cart_page.open_cart()

    checkout_page = CheckoutPage(login_page.page)
    checkout_page.click_checkout()

    checkout_page.fill_information("", "Kharrab", "60000")
    checkout_page.continue_checkout()

    expect(checkout_page.error_message).to_have_text(
        "Error: First Name is required"
    )


def test_checkout_missing_last_name(login_page):
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(login_page.page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(login_page.page)
    cart_page.open_cart()

    checkout_page = CheckoutPage(login_page.page)
    checkout_page.click_checkout()

    checkout_page.fill_information("Chaymae", "", "60000")
    checkout_page.continue_checkout()

    expect(checkout_page.error_message).to_have_text(
        "Error: Last Name is required"
    )


def test_checkout_missing_postal_code(login_page):
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(login_page.page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(login_page.page)
    cart_page.open_cart()

    checkout_page = CheckoutPage(login_page.page)
    checkout_page.click_checkout()

    checkout_page.fill_information("Chaymae", "Kharrab", "")
    checkout_page.continue_checkout()

    expect(checkout_page.error_message).to_have_text(
        "Error: Postal Code is required"
    )


def test_complete_checkout(login_page):
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(login_page.page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(login_page.page)
    cart_page.open_cart()

    checkout_page = CheckoutPage(login_page.page)
    checkout_page.click_checkout()

    checkout_page.fill_information(
        "Chaymae",
        "Kharrab",
        "60000"
    )

    checkout_page.continue_checkout()
    checkout_page.finish_order()

    expect(checkout_page.complete_title).to_have_text(
        "Thank you for your order!"
    )