from pydantic import BaseModel, StrictFloat, StrictInt, field_validator
from pydantic_core import PydanticCustomError


class TaxData(BaseModel):
    income: StrictFloat  # handles all type validations
    tax_year: StrictInt  # handles all type validations

    @field_validator("income", )
    def validate_income(cls, value):
        """Validates the income field."""
        if value <= 0:
            raise PydanticCustomError(
                'value_error',
                "Income must be a positive number greater than zero"
            )
        return value

    @field_validator("tax_year")
    def validate_tax_year(cls, value):
        """Validates the tax_year field."""
        if value < 2019 or value > 2022:
            raise PydanticCustomError(
                'value_error',
                "Tax year must be a valid integer between 2019 and 2022"
            )
        return value
