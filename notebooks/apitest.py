import os
import json
from yelpapi import YelpAPI

# Reading your API key from config.json
def load_config():
    with open('config.json') as f:
        return json.load(f)

config = load_config()
api_key = config['yelp_api_key']

# Function for searching Yelp
def search_yelp(location, search_term):
    with YelpAPI(api_key) as yelp_api:
        search_results = yelp_api.search_query(term=search_term, location=location)

        # Process the 'search_results' as needed
        # Example (assuming results contains store data):
        stores = search_results['businesses']  # Adjust based on actual results format
        return stores

# Example Usage:
