# 🎭 Project 02 — E-Commerce Playwright Automation Framework

> Part of my 5-Project QA Engineering Portfolio

## 📌 Overview

This project demonstrates a maintainable **end-to-end UI automation framework** for an e-commerce web application using **Python, Playwright, and Pytest**.

The framework is designed around the **Page Object Model (POM)** and covers critical customer workflows from authentication and product discovery through cart, checkout, and order validation.

The project also demonstrates automated test reporting and **CI/CD execution using GitHub Actions**.

---

## 🎯 Objectives

The project demonstrates practical experience in:

- UI test automation
- End-to-end test automation
- Page Object Model (POM)
- Test framework design
- Reusable page components
- Pytest-based test execution
- Functional UI validation
- Authentication and security validation
- HTML test reporting
- CI/CD test execution
- Automated regression coverage

---

## 🛒 Application Workflows Covered

The automation framework covers the following e-commerce workflows:

| Area | Coverage |
|:--------------------|:----------------------------------------|
| Authentication | User login |
| Product Listing | Product browsing and validation |
| Product Sorting | Sorting functionality |
| Product Details | Product information validation |
| Shopping Cart | Add/manage cart items |
| Checkout | Checkout workflow |
| Order | Order validation |
| Security | Authentication/security scenarios |
| End-to-End | Complete customer purchase journey |

---

## 🧪 Automation Coverage

### Functional UI Automation

- Login
- Product listing
- Product sorting
- Product details
- Shopping cart
- Checkout
- Order validation

### Security / Authentication

- Authentication-related scenarios
- Security validation

### End-to-End

The framework includes an end-to-end customer purchase journey covering the major stages of an e-commerce transaction.

---

## 🏗️ Framework Architecture

The framework follows the **Page Object Model (POM)** to separate page-level functionality from test scenarios.

```
Test Cases
     ↓
Pytest
     ↓
Page Objects
     ↓
Playwright
     ↓
E-Commerce Web Application
```

This structure helps improve:

- Maintainability
- Reusability
- Readability
- Test organization
- Ease of future test expansion

---

## 📁 Framework Structure

```
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
```

---

## 🧩 Page Object Model

The framework separates page interactions into dedicated page classes.

Examples include:

- `login_page.py`
- `products_page.py`
- `cart_page.py`
- `checkout_page.py`

Test cases consume these page objects rather than placing all UI interaction logic directly inside the test scripts.

This approach supports a more maintainable and scalable automation framework.

---

## 📊 Test Reporting

The framework generates HTML test reports to provide visibility into test execution results.

Report output:

```
reports/
└── test-report.html
```

The reports can be used to review:

- Test execution status
- Passed tests
- Failed tests
- Test-level results
- Overall automation execution

---

## 🔄 CI/CD Integration

The project is integrated with GitHub Actions to automatically execute the Playwright test suite when changes are pushed to the repository.

The CI pipeline has been verified through GitHub Actions execution.

This demonstrates how automated UI tests can be incorporated into a CI/CD workflow rather than being executed only manually on a local machine.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|:--------------------|:----------------------------------------|
| Python | Programming language |
| Playwright | Browser automation |
| Pytest | Test framework |
| pytest-playwright | Playwright integration with Pytest |
| Page Object Model | Framework design pattern |
| HTML Reports | Test execution reporting |
| GitHub Actions | CI/CD automation |

---

## ▶️ How to Run

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

Run the complete test suite:

```bash
pytest
```

Generate the HTML report:

```bash
pytest --html=reports/test-report.html --self-contained-html
```

---

## 💼 Skills Demonstrated

**Test Automation**
- Python
- Playwright
- Pytest
- pytest-playwright
- UI automation
- End-to-end automation
- Functional automation
- Regression automation

**Framework Engineering**
- Page Object Model
- Test organization
- Reusable page components
- Maintainable automation architecture
- Test configuration

**Reporting & CI/CD**
- Test reporting
- CI/CD
- GitHub Actions
- Automated test execution
- CI pipeline validation
- Continuous testing

---

## 🎯 Key Takeaway

This project demonstrates the ability to build and maintain a structured Playwright UI automation framework rather than simply writing individual automation scripts.

It brings together:

**Page Object Model → Pytest → Playwright → Functional UI Automation → Reporting → CI/CD**

The project serves as practical Proof of Work demonstrating modern UI automation and continuous testing practices.

---

## 👨‍💻 Author

**Govind**
QA Engineering | Test Automation | API | Performance | Security
