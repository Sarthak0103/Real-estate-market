import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the target URL (example real estate website)
url = 'https://www.example.com/real-estate-listings'

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract property listings (modify selectors based on actual HTML structure)
properties = soup.find_all('div', class_='property-listing')

# Create lists to store extracted data
property_names = []
prices = []
locations = []
sizes = []

# Loop through each property and extract relevant data
for property in properties:
    name = property.find('h2', class_='property-name').text.strip()
    price = property.find('span', class_='property-price').text.strip()
    location = property.find('span', class_='property-location').text.strip()
    size = property.find('span', class_='property-size').text.strip()
    
    property_names.append(name)
    prices.append(price)
    locations.append(location)
    sizes.append(size)

# Create a DataFrame from the extracted data
data = pd.DataFrame({
    'Name': property_names,
    'Price': prices,
    'Location': locations,
    'Size': sizes
})

# Save the data to a CSV file
data.to_csv('real_estate_data.csv', index=False)

print("Scraping complete. Data saved to 'real_estate_data.csv'.")
