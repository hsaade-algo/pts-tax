from flask import request, jsonify
import logging

from app import app
from . import models, controllers

logging.basicConfig(level=logging.INFO)


@app.route("/calculate-tax", methods=["POST"])
def calculate_tax():
    """
    API endpoint to calculate tax for a given income and tax year.

    Returns:
        JSON response with tax details or an error message.
    """
    data = request.json
    tax_year = data.get("tax_year")
    income = data.get("income")

    # Validate input
    data = models.TaxData(tax_year=tax_year, income=income)

    # Calculate tax
    resp = controllers.generate_tax_data(income, tax_year)

    if "error" in resp:
        return jsonify(resp), 500

    return jsonify(resp), 200
