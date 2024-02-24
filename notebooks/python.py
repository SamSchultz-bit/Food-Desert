# Imports
from bs4 import BeautifulSoup
import time 
import pandas as pd 
import os

# Function to extract listing links
def get_listing_links(search_url):
    response = requests.get(search_url)
    response.raise_for_status() 

    soup = BeautifulSoup(response.content, 'html.parser')

    # *** TROUBLESHOOTING:  ***
    # Print the raw HTML of listings to aid with CSS Selector refinement
    print(soup.select("div.container__098Hl"))  # Adjust CSS selector if needed

    links = []
    for listing in listings:
        link = listing.find('a', class_='css-1m051bw')['href']  
        links.append(base_url + link)

    return links 

# Function to scrape store details 
def extract_store_details(store_url):
    response = requests.get(store_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    store_data = {}

    # PLACEHOLDER: Replace with your CSS selectors 
    store_data['name'] = soup.select_one('h1.css-m7s08c').text.strip() 
    store_data['address'] = soup.select_one('address.css-1h1j0l3').get_text(strip=True)

    # ... Add category extraction (might need more complex logic) ...

    return store_data

# Main scraping function
def scrape_yelp(location, search_term):
    results = []
    start = 0
    search_url = f"{base_url}/search?find_desc={search_term}&find_loc={location}&start={start}"

    while True:
        listing_links = get_listing_links(search_url)

        for link in listing_links:
            store_data = extract_store_details(link)
            results.append(store_data)

        start += 10  
        time.sleep(2) 

        if not listing_links: 
            break 

    # Create DataFrame and save results
    df = pd.DataFrame(results) 
    output_folder = 'data/raw'
    output_filename = 'yelp_stores_minneapolis.csv'
    output_path = os.path.join(output_folder, output_filename)
    os.makedirs(output_folder, exist_ok=True) 
    df.to_csv(output_path, index=False) 

# Set your parameters
base_url = "https://www.yelp.com"
location = "Minneapolis, MN"
search_term = "grocery store"

# Start scraping!
scrape_yelp(location, search_term)
