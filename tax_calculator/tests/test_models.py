import pytest
from pydantic import ValidationError
from tax_calculator.models import TaxData


def test_valid_tax_data():
    """Tests valid tax data input."""
    data = TaxData(income=50000, tax_year=2022)
    assert data.income == 50000.0
    assert data.tax_year == 2022


def test_invalid_income():
    """Tests invalid income input."""
    with pytest.raises(ValidationError) as exc:
        TaxData(income=None, tax_year=2022)

    with pytest.raises(ValidationError):
        TaxData(income="invalid", tax_year=2022)

    with pytest.raises(ValidationError):
        TaxData(income=True, tax_year=2022)

    with pytest.raises(ValidationError):
        TaxData(income=-1, tax_year=2022)


def test_invalid_tax_year():
    """Tests invalid tax year input."""
    with pytest.raises(ValidationError):
        TaxData(income=50000, tax_year=None)

    with pytest.raises(ValidationError):
        TaxData(income=50000, tax_year="invalid")

    with pytest.raises(ValidationError):
        TaxData(income=50000, tax_year=2018)

    with pytest.raises(ValidationError):
        TaxData(income=50000, tax_year=2023)
