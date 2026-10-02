# MLOps Lab 1 - Temperature Converter

This project is based on Lab 1 from the MLOps course repository.

## Project Overview

The original lab used a calculator application.

For my modified version, I created a temperature converter that supports:

- Celsius to Fahrenheit
- Fahrenheit to Celsius
- Celsius to Kelvin
- Kelvin to Celsius
- Input validation
- Absolute-zero validation

## Testing

This project includes tests using:

- Pytest
- Python Unittest

To run Pytest:

```bash
pytest
```

To run Unittest:

```bash
python -m unittest test.test_unittest
```

## GitHub Actions

GitHub Actions are configured to automatically run:

- Pytest
- Unittest

The workflows run when changes are pushed to the `main` branch or when a pull request targets `main`.

## Project Structure

```text
mlop_lab1/
├── .github/
│   └── workflows/
│       ├── pytest_action.yml
│       └── unittest_action.yml
├── data/
│   └── __init__.py
├── src/
│   ├── __init__.py
│   └── converter.py
├── test/
│   ├── __init__.py
│   ├── test_pytest.py
│   └── test_unittest.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Modification from Original Lab

The original lab used calculator functions.

This version replaces the calculator with a temperature converter and includes new test cases for the conversion functions.
