from tax_calculator.controllers import generate_tax_data


def test_generate_tax_data_success(mock_tax_api_success):
    """Test tax calculation when the API responds successfully."""
    response = generate_tax_data(income=75000, tax_year=2022)
    assert "total_tax" in response
    assert response["total_tax"] > 0


def test_generate_tax_data_failure(mock_tax_api_failure):
    """Test tax calculation when the API returns a 500 error."""
    response = generate_tax_data(income=75000, tax_year=2022)
    assert "error" in response
    assert response["error"]["message"] in [
        "Failed to connect to tax API.",
        "Tax service is currently unavailable."
    ]
