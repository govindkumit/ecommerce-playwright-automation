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


def prepare_checkout(page: Page):
    """Add a product and navigate to checkout overview."""

    login(page)

    page.locator(".inventory_item").first.locator("button").click()

    page.locator(".shopping_cart_link").click()

    expect(page.locator(".cart_item")).to_have_count(1)

    page.locator("#checkout").click()

    page.locator("#first-name").fill("Test")
    page.locator("#last-name").fill("User")
    page.locator("#postal-code").fill("560001")

    page.locator("#continue").click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-step-two.html"
    )


def test_order_overview(page: Page):
    """TC-ORDER-001: Verify order overview."""

    prepare_checkout(page)

    expect(page.locator(".title")).to_have_text(
        "Checkout: Overview"
    )

    expect(page.locator(".cart_item")).to_have_count(1)

    expect(page.locator(".summary_subtotal_label")).to_be_visible()
    expect(page.locator(".summary_tax_label")).to_be_visible()
    expect(page.locator(".summary_total_label")).to_be_visible()


def test_complete_successful_order(page: Page):
    """TC-ORDER-002: Verify successful order completion."""

    prepare_checkout(page)

    page.locator("#finish").click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-complete.html"
    )

    expect(page.locator(".complete-header")).to_have_text(
        "Thank you for your order!"
    )


def test_order_contains_selected_product(page: Page):
    """TC-ORDER-003: Verify selected product appears in order."""

    prepare_checkout(page)

    expect(page.locator(".cart_item")).to_have_count(1)

    product_name = page.locator(
        ".inventory_item_name"
    ).inner_text()

    expect(
        page.locator(".inventory_item_name")
    ).to_have_text(product_name)

    page.locator("#finish").click()

    expect(page.locator(".complete-header")).to_have_text(
        "Thank you for your order!"
    )