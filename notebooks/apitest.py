import os
import json
import pandas as pd
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

    results = []
    for store in search_results['businesses']:
        results.append({
            'name': store['name'],
            'address': store['location']['display_address'], 
            'rating': store['rating'],
            'price': store.get('price', 'Price Unavailable'),
            'phone': store['phone'],
            'latitude': store['coordinates']['latitude'],  
            'longitude': store['coordinates']['longitude'],  
            'yelp_url': store['url'] 
        })
    return pd.DataFrame(results)

# Example Usage:
stores_df = search_yelp('Minneapolis, MN', 'grocery store')
print(stores_df)