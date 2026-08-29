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


def test_product_page_loads(page: Page):
    """TC-PROD-001: Verify product page loads successfully."""

    login(page)

    expect(page.locator(".title")).to_have_text("Products")
    expect(page.locator(".inventory_list")).to_be_visible()


def test_product_list_is_displayed(page: Page):
    """TC-PROD-002: Verify products are displayed."""

    login(page)

    products = page.locator(".inventory_item")

    expect(products).to_have_count(6)


def test_product_information_is_displayed(page: Page):
    """TC-PROD-003: Verify product name, price and description."""

    login(page)

    first_product = page.locator(".inventory_item").first

    expect(first_product.locator(".inventory_item_name")).to_be_visible()
    expect(first_product.locator(".inventory_item_desc")).to_be_visible()
    expect(first_product.locator(".inventory_item_price")).to_be_visible()


def test_product_details_page(page: Page):
    """TC-PROD-004: Verify user can open product details."""

    login(page)

    first_product = page.locator(".inventory_item").first

    product_name = first_product.locator(
        ".inventory_item_name"
    ).inner_text()

    first_product.locator(".inventory_item_name").click()

    expect(page.locator(".inventory_details_name")).to_have_text(
        product_name
    )

    expect(page.locator(".inventory_details_desc")).to_be_visible()
    expect(page.locator(".inventory_details_price")).to_be_visible()