def test_api_success(client):
    """Tests API with valid data."""
    response = client.post(
        "/calculate-tax",
        json={"income": 75000.0, "tax_year": 2022}
    )
    assert response.status_code == 200
    assert "total_tax" in response.json


def test_api_invalid_tax_year(client):
    """Tests API with an invalid tax year."""
    response = client.post(
        "/calculate-tax", json={"income": 75000.0, "tax_year": 2025}
    )
    assert response.status_code == 400
    assert "error" in response.json
