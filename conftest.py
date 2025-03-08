import pytest
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
