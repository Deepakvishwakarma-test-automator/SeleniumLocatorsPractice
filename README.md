Selenium Automation Framework

A robust and scalable UI test automation framework built using Python, Selenium WebDriver, Pytest, and the Page Object Model (POM) design pattern. 
This framework is designed to improve test maintainability, reusability, and reporting while enabling efficient end-to-end web application testing.



* Selenium WebDriver for browser automation
* Pytest test execution and fixtures
* Page Object Model (POM) architecture
* Centralized locator management
* Cross-browser support
* Allure reporting integration
* HTML test reports
* Reusable utilities and test components
* Easy-to-maintain project structure
* Scalable framework for large automation suites

# Tech Stack used 

* Python 3.x
* Selenium WebDriver
* Pytest
* Allure Reports (Yet to be wired up)
* Pytest HTML Reports
* ChromeDriver / WebDriver Manager

## Project Structure

project-root/
│
├── pages/
│   ├── pages/
│   │   ├── landing_page.py
│   │   └── ...
│   │
│   └── locators/
│       ├── landing_page_locators.py
│       └── ...
│
├── test/
│   ├── test_landing_page.py
│   └── ...
│
├── reports/
│   ├── allure-results/
│   └── html-reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md


## Framework Design

The framework follows the **Page Object Model (POM)** pattern:

* Page classes contain business actions and page-specific methods.
* Locator classes store element locators separately.
* Tests remain clean and focused on validation.
* Changes in UI locators require updates only in locator files.

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest test/test_landing_page.py
```

Run tests with verbose output:

```bash
pytest -v
```

## Generate Allure Reports

Execute tests:

```bash
pytest --alluredir=reports/allure-results
```

Generate report:

```bash
allure serve reports/allure-results
```

Or:

```bash
allure generate reports/allure-results --clean -o reports/allure-report
```

## Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

## Best Practices Followed

* Separation of test logic and page actions
* Reusable page methods
* Single responsibility principle
* Maintainable locator strategy
* Meaningful test naming conventions
* Automated reporting
* Scalable folder structure

## Sample Test

```python
def test_landing_page(driver):
    landing_page = LandingPage(driver)

    assert landing_page.get_title() == "The Internet"
```

## Future Enhancements

* CI/CD integration with GitHub Actions
* Docker support
* Parallel execution with Pytest-xdist
* Environment-based configuration
* Logging framework integration
* Screenshot capture on failure
* Cross-browser execution matrix

## Author

Deepak

## License

This project is intended for learning, demonstration, and automation framework development purposes.
