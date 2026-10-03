from playwright.sync_api import Page


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

        self.checkout_button = page.locator("#checkout")
        self.checkout_title = page.locator(".title")

        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")

        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")

        self.error_message = page.locator("[data-test='error']")
        self.complete_title = page.locator(".complete-header")

    def click_checkout(self):
        self.checkout_button.click()

    def continue_checkout(self):
        self.continue_button.click()

    def fill_information(self, first_name, last_name, postal_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def finish_order(self):
        self.finish_button.click()