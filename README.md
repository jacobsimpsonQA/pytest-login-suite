# Pytest Login Test Suite

## Overview
A Python + Selenium test suite using `pytest` to validate login functionality on a demo site.

## Project Structure

- `conftest.py`: Pytest fixture that sets up and tears down the ChromeDriver instance
- `utils.py`: Reusable `login()` function shared across tests
- `tests/`
  - `test_login_valid.py`: Valid credentials
  - `test_login_invalid.py`: Invalid password
  - `test_login_blank.py`: Both fields blank
- `requirements.txt`: Project dependencies
- `pytest.ini`: Pytest config

## How to Run

1. Create a virtual environment and activate it:
   python3 -m venv venv
   source venv/bin/activate

2. Install required packages:
   pip install -r requirements.txt

3. Run all tests:
   pytest

## Author
Jacob Simpson – QA Engineer  
https://github.com/jacobsimpsonQA
