from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

        self.add_backpack_button = page.locator(
            "#add-to-cart-sauce-labs-backpack"
        )
        self.add_bike_light_button = page.locator(
            "#add-to-cart-sauce-labs-bike-light"
        )

    def add_backpack_to_cart(self):
        self.add_backpack_button.click()

    def add_bike_light_to_cart(self):
        self.add_bike_light_button.click()