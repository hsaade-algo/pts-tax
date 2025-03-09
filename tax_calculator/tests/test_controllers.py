from tax_calculator.controllers import generate_tax_data


def test_generate_tax_data_success(mock_tax_api_success):
    """Tests tax calculation when the API responds successfully."""
    response = generate_tax_data(income=75000, tax_year=2022)
    assert "total_tax" in response
    assert response["total_tax"] == 12614.16


def test_generate_tax_data_with_invalid_income():
    """Tests tax calculation when the income is invalid."""
    response = generate_tax_data(income="invalid", tax_year=2022)
    assert "error" in response

    response = generate_tax_data(income=-1, tax_year=2022)
    assert "error" in response

    # response = generate_tax_data(income=None, tax_year=2022)
    # assert "error" in response


def test_generate_tax_data_with_api_failure(mock_tax_api_failure):
    """Tests tax calculation when the API returns a 500 error."""
    response = generate_tax_data(income=75000, tax_year=2022)
    assert "error" in response
    assert response["error"]["message"] in [
        "Failed to connect to tax API.",
        "Tax service is currently unavailable."
    ]
