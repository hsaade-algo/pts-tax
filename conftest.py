import pytest
import requests_mock

from app import app


"""
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
            json={
                "tax_brackets": [
                    {
                        "max": 50197,
                        "min": 0,
                        "rate": 0.15
                    },
                    {
                        "max": 100392,
                        "min": 50197,
                        "rate": 0.205
                    },
                    {
                        "max": 155625,
                        "min": 100392,
                        "rate": 0.26
                    },
                    {
                        "max": 221708,
                        "min": 155625,
                        "rate": 0.29
                    },
                    {
                        "min": 221708,
                        "rate": 0.33
                    }
                ]
            },
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
