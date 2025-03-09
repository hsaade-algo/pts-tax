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


def test_api_invalid_data(client):
    """Tests API with invalid data."""
    # Region Invalid Income
    response = client.post(
        "/calculate-tax", json={"income": "invalid", "tax_year": 2022}
    )
    assert response.status_code == 400
    assert "error" in response.json

    response = client.post(
        "/calculate-tax", json={"income": -1, "tax_year": 2022}
    )
    assert response.status_code == 400
    assert "error" in response.json

    response = client.post(
        "/calculate-tax", json={"income": None, "tax_year": 2022}
    )
    assert response.status_code == 400
    assert "error" in response.json
    # Endregion Invalid Income

    # Region Invalid Tax Year
    response = client.post(
        "/calculate-tax", json={"income": 75000.0, "tax_year": "invalid"}
    )
    assert response.status_code == 400
    assert "error" in response.json

    response = client.post(
        "/calculate-tax", json={"income": 75000.0, "tax_year": 2018}
    )
    assert response.status_code == 400
    assert "error" in response.json

    response = client.post(
        "/calculate-tax", json={"income": 75000.0, "tax_year": 2023}
    )
    assert response.status_code == 400
    assert "error" in response.json

    response = client.post(
        "/calculate-tax", json={"income": 75000.0, "tax_year": None}
    )
    assert response.status_code == 400
    assert "error" in response.json
    # Endregion Invalid Tax Year

    # Region Invalid Income and Tax Year
    response = client.post(
        "/calculate-tax", json={"income": None, "tax_year": None}
    )
    assert response.status_code == 400
    assert "error" in response.json

    response = client.post(
        "/calculate-tax", json={"income": None, "tax_year": "invalid"}
    )
    assert response.status_code == 400
    assert "error" in response.json

    response = client.post(
        "/calculate-tax", json={"income": "invalid", "tax_year": "invalid"}
    )
    assert response.status_code == 400
    assert "error" in response.json

    response = client.post(
        "/calculate-tax", json={"income": "invalid", "tax_year": None}
    )
    assert response.status_code == 400
    assert "error" in response.json
    # Endregion Invalid Income and Tax Year
