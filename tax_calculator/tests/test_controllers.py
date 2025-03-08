import pytest

from tax_calculator.controllers import generate_tax_data


# def test_generate_tax_data():
#     resp = generate_tax_data(50000, 2022)
#     assert "error" not in resp

#     with pytest.raises(ZeroDivisionError):
#         resp = generate_tax_data(0, 2022)
#     # assert "error" in resp

#     resp = generate_tax_data(-1, 2022)
#     assert "error" in resp

#     resp = generate_tax_data(50000, 2018)
#     assert "error" in resp

#     resp = generate_tax_data(50000, 2023)
#     assert "error" in resp

