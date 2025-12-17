from backend.api_handler import get_currency_data
import json

currencies_file = "currency.json"
currencies = json.load(open(currencies_file, "r"))
rates = currencies.get("conversion_rates", {})


def check_and_update_currency_data():
    if not get_currency_data():
        # Check if currency data was fetched and saved successfully
        print("Failed to update currency data. Exiting.")
        exit(1)


def convert_currency(amount, from_currency, to_currency):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Invalid currency code provided.")

    # Convert amount to USD first, then to target currency
    amount_in_usd = amount / rates[from_currency]
    converted_amount = round(amount_in_usd * rates[to_currency], 2)

    return converted_amount


if __name__ == "__main__":
    print(convert_currency(100, "USD", "EGP"))
    print("Warning: This conversion might not be up-to-date due to outdated currency rates and api content misinformation.")