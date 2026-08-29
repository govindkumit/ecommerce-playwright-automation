import pytest
from playwright.sync_api import Page, expect


BASE_URL = "https://www.saucedemo.com/"

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


def test_valid_login(page: Page):
    """TC-LOGIN-001: Verify login with valid credentials."""

    page.goto(BASE_URL)

    page.locator("#user-name").fill(VALID_USERNAME)
    page.locator("#password").fill(VALID_PASSWORD)
    page.locator("#login-button").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_invalid_username(page: Page):
    """TC-LOGIN-002: Verify login with invalid username."""

    page.goto(BASE_URL)

    page.locator("#user-name").fill("invalid_user")
    page.locator("#password").fill(VALID_PASSWORD)
    page.locator("#login-button").click()

    error_message = page.locator("[data-test='error']")

    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text(
        "Username and password do not match"
    )


def test_invalid_password(page: Page):
    """TC-LOGIN-003: Verify login with invalid password."""

    page.goto(BASE_URL)

    page.locator("#user-name").fill(VALID_USERNAME)
    page.locator("#password").fill("invalid_password")
    page.locator("#login-button").click()

    error_message = page.locator("[data-test='error']")

    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text(
        "Username and password do not match"
    )


def test_empty_username(page: Page):
    """TC-LOGIN-004: Verify login with empty username."""

    page.goto(BASE_URL)

    page.locator("#password").fill(VALID_PASSWORD)
    page.locator("#login-button").click()

    error_message = page.locator("[data-test='error']")

    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text(
        "Username is required"
    )


def test_empty_password(page: Page):
    """TC-LOGIN-005: Verify login with empty password."""

    page.goto(BASE_URL)

    page.locator("#user-name").fill(VALID_USERNAME)
    page.locator("#login-button").click()

    error_message = page.locator("[data-test='error']")

    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text(
        "Password is required"
    )