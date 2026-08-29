# E-Commerce Playwright Automation Framework

End-to-end UI automation framework for an e-commerce web application using **Python, Playwright, and Pytest**.

## Project Overview

This project demonstrates a maintainable Playwright automation framework covering critical e-commerce workflows including:

- User Login
- Product Listing
- Product Sorting
- Product Details
- Shopping Cart
- Checkout
- Order Validation
- Security / Authentication
- End-to-End Customer Purchase Journey

## Tech Stack

- Python
- Playwright
- Pytest
- pytest-playwright
- HTML Test Reports
- Page Object Model (POM)

## Framework Structure

```text
ecommerce-playwright-automation/
│
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_sorting.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_order.py
│   ├── test_security.py
│   └── test_e2e.py
│
├── reports/
│   └── test-report.html
│
├── screenshots/
├── utils/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md