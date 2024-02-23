# Food-Desert and Grocery Opportunity Analysis

Locating and analysing causes of food deserts and to find opportunities for grocers.

## Phase 1: Data Acquisition & Preprocessing

### Scraping Yelp:

- Write scripts using BeautifulSoup to extract store listings, addresses, and categories.
- Implement pagination and respectful request intervals to avoid blocking.

### USDA Atlas Download:

- Download relevant food desert datasets.
  -Convert into usable formats.

### Census Data Extraction:

- Select desired demographic variables (e.g., income, population density).
- Download and format as DataFrames.

### Cleaning & Merging:

- Thoroughly clean addresses (standardization, fixing typos).
- Remove duplicate store entries.
- Experiment with joining datasets based on location.

## Phase 2: Geocoding & Initial Mapping

### API Choice:

- Decide on OpenStreetMap (Nominatim) vs. another provider. Set up API keys if required.
- Write geocoding functions to batch-convert addresses to latitude/longitude.
- Handle rate limiting and potential errors gracefully.

### Basic Nationwide Visualization:

- Create a Plotly map of the US.
  Overlay USDA food deserts.
- Plot initial store locations (you can color-code by chain vs. independent later).

## Phase 3: Zooming & Layering

### Data Structuring

- Divide data into states, and potentially further into cities/regions. Consider file storage (separate CSVs, SQLite database, etc.).

### Zoom Functionality:

- Implement Plotly callbacks.
- User selects a state -> Load the respective data chunk, generate a new map.
- Repeat for the city/region selection within a state.

### Distinct Layers:

- Differentiate markers for store types and food banks.
- Add census data as overlays (color gradients or choropleth maps)

## Phase 4: Analysis & Insights

### Target Location Logic:

- Decide on your metrics (distance-based, population density within underserved areas, etc.)
- Code functions to calculate and highlight potential store locations.

### Accessibility:

- Explore OpenStreetMap's routing engine to add simple travel estimations.

### Report Generation:

- Use Jupyter Notebook or similar to document your methods, analysis, and key findings.

### Simple Dashboard (Optional):

- If time allows, use a tool like Dash to create a web interface, enhancing project appeal.
