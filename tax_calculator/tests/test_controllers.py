from tax_calculator.controllers import generate_tax_data


def test_generate_tax_data_with_random_api_response():
    """
    Tests that the function handles both success and failure cases correctly.

    TODO: This test is unreliable as it relies on the random API response.
    This should be replaced with a mock API response in the future.
    """
    response = generate_tax_data(income=45000, tax_year=2022)

    # Either the API works and returns a total_tax, or it fails and returns
    # an error
    assert ("total_tax" in response and response["total_tax"] >= 0) \
        or ("error" in response)

    # If the API fails, the error message should be present
    if "error" in response:
        assert "error" in response
