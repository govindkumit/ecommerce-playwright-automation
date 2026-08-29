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


def get_product_names(page: Page):
    """Return product names in their current display order."""

    return page.locator(".inventory_item_name").all_inner_texts()


def get_product_prices(page: Page):
    """Return product prices as floating-point numbers."""

    prices = page.locator(".inventory_item_price").all_inner_texts()
    return [float(price.replace("$", "")) for price in prices]


def test_sort_products_name_ascending(page: Page):
    """TC-SORT-001: Verify products can be sorted A to Z."""

    login(page)

    page.locator(".product_sort_container").select_option("az")

    product_names = get_product_names(page)

    assert product_names == sorted(product_names)


def test_sort_products_name_descending(page: Page):
    """TC-SORT-002: Verify products can be sorted Z to A."""

    login(page)

    page.locator(".product_sort_container").select_option("za")

    product_names = get_product_names(page)

    assert product_names == sorted(product_names, reverse=True)


def test_sort_products_price_ascending(page: Page):
    """TC-SORT-003: Verify products can be sorted by price low to high."""

    login(page)

    page.locator(".product_sort_container").select_option("lohi")

    product_prices = get_product_prices(page)

    assert product_prices == sorted(product_prices)


def test_sort_products_price_descending(page: Page):
    """TC-SORT-004: Verify products can be sorted by price high to low."""

    login(page)

    page.locator(".product_sort_container").select_option("hilo")

    product_prices = get_product_prices(page)

    assert product_prices == sorted(product_prices, reverse=True)