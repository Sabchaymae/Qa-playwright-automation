from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.backpack_item = page.locator(
            "[data-test='inventory-item-name']"
        ).filter(has_text="Sauce Labs Backpack")
        self.backpack_quantity = page.locator("[data-test='item-quantity']")
        self.remove_backpack_button = page.locator("#remove-sauce-labs-backpack")
        self.backpack_price = page.locator(
    ".cart_item"
).filter(
    has_text="Sauce Labs Backpack"
).locator(
    "[data-test='inventory-item-price']"
)

    def open_cart(self):
        self.cart_link.click()