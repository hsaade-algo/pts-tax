def test_api_success(client, mock_tax_api_success):
    """Tests API with valid data and mocked successful tax API."""
    response = client.post(
        "/calculate-tax",
        json={"income": 75000.0, "tax_year": 2022}
    )
    assert response.status_code == 200
    assert "total_tax" in response.json


def test_api_failure(client, mock_tax_api_failure):
    """Tests API with a failing tax API (500 error)."""
    response = client.post(
        "/calculate-tax", json={"income": 75000.0, "tax_year": 2022}
    )
    assert response.status_code == 500
    assert "error" in response.json
