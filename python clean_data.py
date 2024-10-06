import pandas as pd

# Load the scraped data
data = pd.read_csv('real_estate_data.csv')

# Clean the data (example steps)
data['Price'] = data['Price'].str.replace(',', '').str.replace('$', '').astype(float)
data['Size'] = data['Size'].str.replace('sqft', '').astype(float)
data['Location'] = data['Location'].str.strip()

# Handle missing values
data.dropna(inplace=True)

# Save the cleaned data
data.to_csv('cleaned_real_estate_data.csv', index=False)

print("Data cleaning complete. Cleaned data saved to 'cleaned_real_estate_data.csv'.")
