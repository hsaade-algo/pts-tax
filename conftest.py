import pytest
import requests_mock

from app import app


"""
Pytest fixture to create a test client for the Flask app.
scope="module" ensures that the client is created once per module, instead of
per test, and therefore speeds up test execution.
"""


@pytest.fixture(scope="module")
def client():
    """Creates a test client for Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="module")
def mock_tax_api_success():
    """Mocks the tax API with a successful response."""
    with requests_mock.Mocker() as mocker:
        mocker.get(
            "http://localhost:5001/tax-calculator/tax-year/2022",
            json={"tax_brackets": [{"min": 0, "max": 50000, "rate": 0.1}]},
            status_code=200
        )
        yield mocker


@pytest.fixture(scope="module")
def mock_tax_api_failure():
    """Mocks the tax API with a failure response (500 error)."""
    with requests_mock.Mocker() as mocker:
        mocker.get(
            "http://localhost:5001/tax-calculator/tax-year/2022",
            json={"errors": [{"message": "Internal Server Error"}]},
            status_code=500
        )
        yield mocker
