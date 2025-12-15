import requests as req
import json
import os

url = r'https://v6.exchangerate-api.com/v6/2baa9d40347d0d8b176f2069/latest/USD'

def get_currency_data():

    try:
        response = req.get(url)
        json.dump(
            dict(response.json()),
            open("currency.json", "w+"),
            indent=4
            )

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Failed to fetch or save currency data. Using cached data if available.")

        if os.path.exists("currency.json"):
            print("There is a cached currency file available. Using cached data.")
        else:
            print("No cached currency file found. Please check your internet connection.")
            exit(5)
            return False

    # clean up the json file by removing unnecessary data
    try:
        with open("currency.json", "r") as f:
            data = json.load(f)

        cleaned_data = {
            "conversion_rates": data.get("conversion_rates", {})
        }

        with open("currency.json", "w") as f:
            json.dump(cleaned_data, f, indent=4)
    except Exception as e:
        print(f"An error occurred during cleanup: {e}")
        print("The currency data may be incomplete or corrupted.")
        return False
    return True
if __name__ == "__main__":
    get_currency_data()