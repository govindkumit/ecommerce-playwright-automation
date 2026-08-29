from playwright.sync_api import Page, expect


BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def login(page: Page):
    """Login with a valid user."""

    page.goto(BASE_URL)

    page.locator("#user-name").fill(USERNAME)
    page.locator("#password").fill(PASSWORD)
    page.locator("#login-button").click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )


def add_product_and_open_checkout(page: Page):
    """Add one product and navigate to checkout."""

    login(page)

    page.locator(".inventory_item").first.locator("button").click()

    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    page.locator(".shopping_cart_link").click()

    expect(page.locator(".cart_item")).to_have_count(1)

    page.locator("#checkout").click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-step-one.html"
    )


def test_navigate_to_checkout(page: Page):
    """TC-CHECK-001: Verify user can navigate to checkout."""

    add_product_and_open_checkout(page)

    expect(page.locator(".title")).to_have_text(
        "Checkout: Your Information"
    )


def test_checkout_with_valid_information(page: Page):
    """TC-CHECK-002: Verify checkout with valid information."""

    add_product_and_open_checkout(page)

    page.locator("#first-name").fill("Test")
    page.locator("#last-name").fill("User")
    page.locator("#postal-code").fill("560001")

    page.locator("#continue").click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-step-two.html"
    )

    expect(page.locator(".title")).to_have_text(
        "Checkout: Overview"
    )


def test_checkout_missing_first_name(page: Page):
    """TC-CHECK-003: Verify validation for missing first name."""

    add_product_and_open_checkout(page)

    page.locator("#last-name").fill("User")
    page.locator("#postal-code").fill("560001")

    page.locator("#continue").click()

    error = page.locator("[data-test='error']")

    expect(error).to_be_visible()
    expect(error).to_contain_text("First Name is required")


def test_checkout_missing_last_name(page: Page):
    """TC-CHECK-004: Verify validation for missing last name."""

    add_product_and_open_checkout(page)

    page.locator("#first-name").fill("Test")
    page.locator("#postal-code").fill("560001")

    page.locator("#continue").click()

    error = page.locator("[data-test='error']")

    expect(error).to_be_visible()
    expect(error).to_contain_text("Last Name is required")


def test_checkout_missing_postal_code(page: Page):
    """TC-CHECK-005: Verify validation for missing postal code."""

    add_product_and_open_checkout(page)

    page.locator("#first-name").fill("Test")
    page.locator("#last-name").fill("User")

    page.locator("#continue").click()

    error = page.locator("[data-test='error']")

    expect(error).to_be_visible()
    expect(error).to_contain_text("Postal Code is required")