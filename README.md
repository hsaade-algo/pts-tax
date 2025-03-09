# Tax Calculator API
<br>

## 📌 Overview
The **Tax Calculator API** is a Flask-based service that calculates income tax based on tax brackets for a given year. The API includes:
- A production-ready **Dockerized deployment** using **Gunicorn**.
- **Graceful error handling** for API failures and timeouts.
- **Automated testing with Pytest & requests-mock**.

<br>

## 🚀 Quick Start
### **1️⃣ Running the API in a Production-Like Docker Environment**
To simulate a production deployment with **Gunicorn and Flask**, run:
```bash
docker-compose up --build -d
```

Once the containers are running, access the API at:
```
http://localhost:5000/calculate-tax
```


### **2️⃣ Running the API in Development Mode**
For local development **without Docker**, use Flask’s built-in dev server:
```bash
pip install -r requirements.txt
python app.py
```
The API will be available at:
```
http://localhost:5002/calculate-tax
```

<br>

## 📜 API Documentation
### **Endpoint: `POST /calculate-tax`**
Calculates total tax based on a given income and tax year.

#### **📌 Request Parameters**
| Parameter  | Type    | Required | Description                                      | Example    |
|------------|--------|----------|--------------------------------------------------|------------|
| `income`   | float  | ✅ Yes    | The annual income to calculate tax for.         | `75000.0`  |
| `tax_year` | int    | ✅ Yes    | The tax year to use for calculation (2019-2022). | `2022`     |

#### **📩 Example Request Body (JSON)**
```json
{
  "income": 75000.0,
  "tax_year": 2022
}
```

#### **✅ Response (Success - 200 OK):**
```json
{
  "total_tax": 15000.0,
  "effective_rate": 0.2,
  "marginal_rate": 0.26,
  "tax_bands": [
    {"min": 0, "max": 50000, "tax_amount": 5000.0, "tax_rate": 0.1},
    {"min": 50000, "max": 100000, "tax_amount": 10000.0, "tax_rate": 0.2}
  ]
}
```

#### **❌ Response (Validation Error - 400 Bad Request):**
```json
{
  "error": "Invalid income or tax year"
}
```

#### **❌ Response (Internal Server Error - 500):**
```json
{
  "error": "Tax service is currently unavailable."
}
```

<br>

## ✅ Running Tests
The tests are written in `pytest`, a popular Python testing framework.

To run all tests:

```bash
pytest
```

To list all discovered tests without running them:

```bash
pytest --collect-only
```

### Coverage

To check overall code coverage for the `tax_calculator` package:

```bash
pytest --cov=tax_calculator
```
This will show a coverage summary in the terminal.


### Coverage Exclusions
To exclude specific files from coverage calculation, add them in the `.coveragerc` file.


### Coverage Report

Generate a Coverage Report

Option 1: Terminal

```bash
pytest --cov=tax_calculator --cov-report=term
```

This prints coverage details in the terminal.

Option 2: Generate an HTML Report

```bash
pytest --cov=tax_calculator --cov-report=html
```

Then, open the report:

```bash
open htmlcov/index.html  # On macOS/Linux
start htmlcov/index.html  # On Windows
```

This opens a detailed coverage report in your browser.

<br>

## 🛠 Technologies Used
- **Flask** - Backend framework
- **Gunicorn** - WSGI server for production
- **Docker & Docker Compose** - Containerization
- **Pydantic** - Request validation
- **requests-mock** - Mocking external API calls
- **Pytest & pytest-cov** - Automated testing with coverage
- **Flake8** - Linting