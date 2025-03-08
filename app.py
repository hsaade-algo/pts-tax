from flask import Flask, jsonify
from pydantic import ValidationError

from tax_calculator.error_handlers import format_validation_error


app = Flask(__name__)


@app.errorhandler(ValidationError)
def validation_error(error):
    formatted_errors = format_validation_error(error)
    return jsonify({"error": formatted_errors}), 400


from tax_calculator.routes import *  # noqa


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
