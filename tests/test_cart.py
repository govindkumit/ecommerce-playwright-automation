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


def test_add_one_product_to_cart(page: Page):
    """TC-CART-001: Verify one product can be added to cart."""

    login(page)

    first_product = page.locator(".inventory_item").first
    product_name = first_product.locator(
        ".inventory_item_name"
    ).inner_text()

    first_product.locator("button").click()

    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    page.locator(".shopping_cart_link").click()

    expect(page.locator(".cart_item")).to_have_count(1)
    expect(
        page.locator(".inventory_item_name")
    ).to_have_text(product_name)


def test_cart_count_updates(page: Page):
    """TC-CART-002: Verify cart count after adding multiple products."""

    login(page)

    products = page.locator(".inventory_item")

    products.nth(0).locator("button").click()
    products.nth(1).locator("button").click()

    expect(page.locator(".shopping_cart_badge")).to_have_text("2")


def test_add_multiple_products_to_cart(page: Page):
    """TC-CART-003: Verify multiple products can be added."""

    login(page)

    products = page.locator(".inventory_item")

    products.nth(0).locator("button").click()
    products.nth(1).locator("button").click()
    products.nth(2).locator("button").click()

    page.locator(".shopping_cart_link").click()

    expect(page.locator(".cart_item")).to_have_count(3)


def test_remove_product_from_cart(page: Page):
    """TC-CART-004: Verify a product can be removed from cart."""

    login(page)

    products = page.locator(".inventory_item")

    products.nth(0).locator("button").click()
    products.nth(1).locator("button").click()

    expect(page.locator(".shopping_cart_badge")).to_have_text("2")

    page.locator(".shopping_cart_link").click()

    expect(page.locator(".cart_item")).to_have_count(2)

    page.locator(".cart_item").first.locator("button").click()

    expect(page.locator(".cart_item")).to_have_count(1)
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")


def test_remove_one_product_and_retain_other(page: Page):
    """TC-CART-005: Verify removing one product retains the other."""

    login(page)

    products = page.locator(".inventory_item")

    products.nth(0).locator("button").click()
    products.nth(1).locator("button").click()

    page.locator(".shopping_cart_link").click()

    cart_items = page.locator(".cart_item")

    expect(cart_items).to_have_count(2)

    remaining_product = cart_items.nth(1).locator(
        ".inventory_item_name"
    ).inner_text()

    cart_items.first.locator("button").click()

    expect(page.locator(".cart_item")).to_have_count(1)
    expect(
        page.locator(".inventory_item_name")
    ).to_have_text(remaining_product)


def test_empty_cart(page: Page):
    """TC-CART-006: Verify cart is empty when no product is added."""

    login(page)

    page.locator(".shopping_cart_link").click()

    expect(page.locator(".cart_item")).to_have_count(0)
    expect(page.locator(".cart_list")).to_be_visible()