from playwright.sync_api import expect


def test_login_valid(login_page):
    login_page.login("standard_user", "secret_sauce")

    expect(login_page.page_title).to_have_text("Products")

def test_login_empty_username(login_page):
    login_page.login("", "secret_sauce")

    expect(login_page.error_message).to_have_text("Epic sadface: Username is required")


def test_login_empty_password(login_page):
    login_page.login("standard_user", "")

    expect(login_page.error_message).to_have_text("Epic sadface: Password is required")


def test_login_invalid_username(login_page):
    login_page.login("wrong_user", "secret_sauce")

    expect(login_page.error_message).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )


def test_login_invalid_password(login_page):
    login_page.login("standard_user", "wrong_password")

    expect(login_page.error_message).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )


def test_login_both_fields_empty(login_page):
    login_page.login("", "")

    expect(login_page.error_message).to_have_text("Epic sadface: Username is required")