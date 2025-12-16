# Placeholder module for the Conversion Calculator project.
from ..api_handler import get_currency_data

if not get_currency_data():
# Check if currency data was fetched and saved successfully
    print("Failed to update currency data. Exiting.")
    exit(1)

