# Tax Calculator Tests
<br>

The tests are written in `pytest`, a popular Python testing framework.

To run all tests, run the following command:

```bash
pytest
```

To list all discovered tests without running them:

```bash
pytest --collect-only
```

## Coverage

To check overall code coverage for the `tax_calculator` package, run the following command:

```bash
pytest --cov=tax_calculator
```
This will show a coverage summary in the terminal.


## Coverage Exclusions
To exclude specific files from coverage calculation, add them in the `.coveragerc` file.


## Coverage Report

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
