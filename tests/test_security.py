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


def test_logout_authenticated_user(page: Page):
    """TC-SEC-001: Verify authenticated user can logout."""

    login(page)

    page.locator("#react-burger-menu-btn").click()

    expect(page.locator("#logout_sidebar_link")).to_be_visible()

    page.locator("#logout_sidebar_link").click()

    expect(page).to_have_url(BASE_URL)

    expect(page.locator("#login-button")).to_be_visible()


def test_protected_access_after_logout(page: Page):
    """TC-SEC-002: Verify protected page cannot be accessed after logout."""

    login(page)

    page.locator("#react-burger-menu-btn").click()
    page.locator("#logout_sidebar_link").click()

    expect(page).to_have_url(BASE_URL)

    # Attempt to access the protected inventory page directly.
    page.goto(f"{BASE_URL}inventory.html")

    expect(page).to_have_url(BASE_URL)
    expect(page.locator("#login-button")).to_be_visible()