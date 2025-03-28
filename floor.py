#!/usr/bin/env python3
# coding: utf-8
import os, json, requests, time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(verbose=True, override=True)

# Access the API keys using os.getenv()
os_api_key = os.getenv("API_KEY_OPENSEA")
os_api_version = os.getenv("API_PATH_OPENSEA")
data_folder_path = os.getenv("DATA_FOLDER")


def get_collection_link(slug):
    return f"https://opensea.io/collection/{slug}"


def get_floor_price(slug):
    """Get Collection's Floor Price"""
    url = os_api_version + "/collections/" + slug + "/stats"
    headers = {"accept": "application/json", "x-api-key": os_api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        try:
            json_data = response.json()
            total_stats = json_data.get("total")
            if total_stats:
                floor = total_stats.get("floor_price")
                currency = total_stats.get("floor_price_symbol")
                average_price = total_stats.get("average_price")
                if (
                    floor is not None
                    and currency is not None
                    and average_price is not None
                ):
                    collection_link = get_collection_link(slug)
                    return f"{slug} floor: {floor:.4f} {currency} (avrg:{average_price:.4f}) | {collection_link}"
                else:
                    return f"Error: Missing data in response for {slug}"
            else:
                return f"Error: 'total' key not found in response for {slug}"
        except json.JSONDecodeError:
            return f"Error: Could not decode JSON response for {slug}"
    except requests.exceptions.RequestException as e:
        return f"Error fetching data for {slug}: {e}"


def main(sleep_duration=0):
    try:
        with open(f"{data_folder_path}slugs.json", "r") as f:
            slugs = sorted(json.load(f))
        for slug in slugs:
            floor = get_floor_price(slug)
            print(floor)
            time.sleep(sleep_duration)
    except FileNotFoundError:
        print(f"Error: slugs.json not found at {data_folder_path}")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from slugs.json at {data_folder_path}")
    except Exception as e:
        print(f"An unexpected error occurred in main: {e}")


if __name__ == "__main__":
    sleep_between_requests = 0.618
    main(sleep_between_requests)
