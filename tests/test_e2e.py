from playwright.sync_api import Page, expect


BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def test_complete_customer_purchase_journey(page: Page):
    """
    TC-E2E-001:
    Verify complete customer purchase journey.

    Flow:
    Login → Product Selection → Cart → Checkout
    → Order Overview → Order Completion
    """

    # 1. Login
    page.goto(BASE_URL)

    page.locator("#user-name").fill(USERNAME)
    page.locator("#password").fill(PASSWORD)
    page.locator("#login-button").click()

    expect(page).to_have_url(
        f"{BASE_URL}inventory.html"
    )

    # 2. Select product
    first_product = page.locator(".inventory_item").first

    product_name = first_product.locator(
        ".inventory_item_name"
    ).inner_text()

    first_product.locator("button").click()

    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    # 3. Open cart
    page.locator(".shopping_cart_link").click()

    expect(page).to_have_url(
        f"{BASE_URL}cart.html"
    )

    expect(page.locator(".cart_item")).to_have_count(1)

    expect(
        page.locator(".inventory_item_name")
    ).to_have_text(product_name)

    # 4. Checkout
    page.locator("#checkout").click()

    expect(page).to_have_url(
        f"{BASE_URL}checkout-step-one.html"
    )

    # 5. Enter customer information
    page.locator("#first-name").fill("Test")
    page.locator("#last-name").fill("User")
    page.locator("#postal-code").fill("560001")

    page.locator("#continue").click()

    # 6. Verify order overview
    expect(page).to_have_url(
        f"{BASE_URL}checkout-step-two.html"
    )

    expect(page.locator(".title")).to_have_text(
        "Checkout: Overview"
    )

    expect(page.locator(".cart_item")).to_have_count(1)

    expect(
        page.locator(".inventory_item_name")
    ).to_have_text(product_name)

    expect(page.locator(".summary_subtotal_label")).to_be_visible()
    expect(page.locator(".summary_tax_label")).to_be_visible()
    expect(page.locator(".summary_total_label")).to_be_visible()

    # 7. Complete order
    page.locator("#finish").click()

    expect(page).to_have_url(
        f"{BASE_URL}checkout-complete.html"
    )

    expect(page.locator(".complete-header")).to_have_text(
        "Thank you for your order!"
    )

    expect(page.locator(".complete-text")).to_be_visible()


def test_multiple_product_purchase_journey(page: Page):
    """
    TC-E2E-002:
    Verify purchase journey with multiple products.

    Flow:
    Login → Select multiple products → Cart → Checkout
    → Verify products → Complete order
    """

    # 1. Login
    page.goto(BASE_URL)

    page.locator("#user-name").fill(USERNAME)
    page.locator("#password").fill(PASSWORD)
    page.locator("#login-button").click()

    expect(page).to_have_url(
        f"{BASE_URL}inventory.html"
    )

    # 2. Add two products
    products = page.locator(".inventory_item")

    product_1 = products.nth(0).locator(
        ".inventory_item_name"
    ).inner_text()

    product_2 = products.nth(1).locator(
        ".inventory_item_name"
    ).inner_text()

    products.nth(0).locator("button").click()
    products.nth(1).locator("button").click()

    expect(page.locator(".shopping_cart_badge")).to_have_text("2")

    # 3. Open cart
    page.locator(".shopping_cart_link").click()

    expect(page.locator(".cart_item")).to_have_count(2)

    cart_names = page.locator(
        ".inventory_item_name"
    ).all_inner_texts()

    assert product_1 in cart_names
    assert product_2 in cart_names

    # 4. Checkout
    page.locator("#checkout").click()

    page.locator("#first-name").fill("Test")
    page.locator("#last-name").fill("User")
    page.locator("#postal-code").fill("560001")

    page.locator("#continue").click()

    # 5. Verify both products in order overview
    expect(page).to_have_url(
        f"{BASE_URL}checkout-step-two.html"
    )

    expect(page.locator(".cart_item")).to_have_count(2)

    overview_names = page.locator(
        ".inventory_item_name"
    ).all_inner_texts()

    assert product_1 in overview_names
    assert product_2 in overview_names

    # 6. Complete order
    page.locator("#finish").click()

    expect(page).to_have_url(
        f"{BASE_URL}checkout-complete.html"
    )

    expect(page.locator(".complete-header")).to_have_text(
        "Thank you for your order!"
    )