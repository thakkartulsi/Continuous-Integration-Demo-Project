import pytest
from unittest.mock import patch
import app
import subprocess

# Test successful API response
@patch("app.requests.get")
def test_get_quote_success(mock_get):
    # Mocking a successful response
    mock_response = {
        "content": "Success is not final; failure is not fatal: It is the courage to continue that counts.",
        "author": "Winston Churchill"
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    # Call the function and check if the output is as expected
    quote = app.get_quote()
    expected_output = "**Success is not final; failure is not fatal: It is the courage to continue that counts.**\n\n— *Winston Churchill*"
    assert quote == expected_output, "Test Failed: The quote response is incorrect."

# Test API failure response
@patch("app.requests.get")
def test_get_quote_failure(mock_get):
    # Mocking a failed API response
    mock_get.return_value.status_code = 500  # Simulating a server error

    quote = app.get_quote()
    assert quote == "Oops! Couldn't fetch a quote. Try again!", "Test Failed: API failure handling is incorrect."

# Test if the function handles a missing field in response
@patch("app.requests.get")
def test_get_quote_missing_field(mock_get):
    # Mocking a response missing the 'author' field
    mock_response = {"content": "Life is beautiful."}  # Missing author field
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    quote = app.get_quote()
    # Since the function returns 'Unknown author' for missing author
    assert "Unknown author" in quote, "Test Failed: Function should handle missing fields properly."

# Code quality test using flake8
def test_code_quality():
    """Run flake8 to check for PEP8 compliance."""
    result = subprocess.run(["flake8", "app.py"], capture_output=True, text=True)
    assert result.returncode == 0, f"PEP8 violations found:\n{result.stdout}"

# Static analysis using pylint
def test_static_analysis():
    """Run pylint for static code analysis."""
    result = subprocess.run(["pylint", "app.py"], capture_output=True, text=True)
    assert result.returncode == 0 or result.returncode == 4, f"Pylint issues found:\n{result.stdout}"

if __name__ == "__main__":
    pytest.main()
