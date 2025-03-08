from typing import Dict, Any
import requests
import logging
import time

logging.basicConfig(level=logging.INFO)


def _get_tax_brackets(
        tax_year: int,
        max_retries: int = 1,
        backoff_factor: float = 1.5 # Exponential backoff multiplier
    ) -> Dict[str, Any]:
    """
    Fetches the tax brackets for a given tax year with error handling and
    retries.

    Args:
        tax_year (int): The tax year to fetch the tax brackets for.
        max_retries (int, optional): The maximum number of retries.
            Defaults to 3.
        backoff_factor (float, optional): The backoff factor for exponential
            backoff. Defaults to 1.5.

    Returns:
        dict: A dict containing tax bracket(s) or error message(s).
    """
    BASE_URL = "http://localhost:5001/tax-calculator/"
    TAX_API_URL = f"{BASE_URL}/tax-year/{tax_year}"

    for attempt in range(max_retries):
        try:
            resp = requests.get(TAX_API_URL)
            resp.raise_for_status()
            data = resp.json()

            # Detect API errors (randomly injected)
            if "errors" in data:
                logging.error(f"Tax API returned errors: {data['errors']}")
                return {"error": data["errors"]}

            return data

        except requests.exceptions.HTTPError as http_err:
            logging.error(
                f"(#{attempt + 1}) Server error [{resp.status_code}]"
                f" with details: {str(resp.json())}"
            )
            time.sleep(backoff_factor ** attempt)
            continue  # Retry

        # Fallback
        except Exception as err:
            logging.error(f"Request failed: {err}")
            return {"error": {"message": "Failed to connect to tax API."}}

    logging.error("Max retries reached. API unavailable.")
    return {"error": {"message": "Tax service is currently unavailable."}}


def generate_tax_data(income: float, tax_year: int) -> Dict[str, Any]:
    """
    Generates tax data for a given income and tax year.

    Args:
        income (float): The gross income to calculate the tax for.
        tax_year (int): The tax year to calculate the tax for.

    Returns:
        dict: A dict containing tax data or error messages.
    """
    resp = _get_tax_brackets(tax_year)

    # Handle API errors
    if "error" in resp:
        logging.error(f"Error fetching tax brackets: {resp['error']}")
        return resp
    
    tax_brackets = resp.get("tax_brackets", [])

    # Calculate tax
    tax_data = []
    total_tax = 0
    marginal_rate = 0

    for bracket in tax_brackets:
        min_amt = bracket.get("min", 0)
        max_amt = bracket.get("max", 0)
        band_rate = bracket.get("rate", 0)

        # A band is applicable if the income is greater than its min amount
        if income > min_amt:
            band_amount = min(income, max_amt) - min_amt
            tax_amount = band_amount * band_rate
            total_tax += tax_amount

            tax_data.append({
                "min": min_amt,
                "max": max_amt,
                "tax_amount": round(tax_amount, 2),
                "tax_rate": band_rate
            })

            marginal_rate = band_rate

    data = {
        "tax_bands": tax_data,
        "total_tax": round(total_tax, 2),
        "marginal_rate": marginal_rate,
        "effective_rate": round(total_tax / income, 2)
    }

    return data
