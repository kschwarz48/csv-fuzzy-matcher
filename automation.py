import pandas as pd
from fuzzywuzzy import fuzz

# Load data from master.csv and second.csv
google_sheets_data = pd.read_csv('master.csv', header=7)
excel_data = pd.read_csv('second.csv', header=0)

# Manually map column names of google_sheets_data to match excel_data
google_sheets_data.rename(columns={'DEPARTMENT': 'Dept', 'STYLE DESC.': 'Style Name', 'COLOR DESC.': 'Artwork/Color No/Name', 'IS DATE': 'In Store Date',
                                   'ORDER QTY': 'Qty', 'RETAIL': 'Retail Price', 'SIZE PROFILE': 'Size Range', 'BBR LUC': 'LUC', 'BBR SUC': 'SUC', 'BBR TRANS MODE': 'Trans Mode', 'CHANNEL': 'Channel', 'STYLE NO': 'Style No', 'AC DATE': 'AC Date'}, inplace=True)

columns_to_compare = ['Style No', 'Channel', 'Style Name']

# Preprocess 'Channel' column to consider "US Stores" = "Stores"
google_sheets_data['Channel'] = google_sheets_data['Channel'].str.replace(
    "Stores", "US STORES")

# Convert columns to string type
for col in columns_to_compare:
    google_sheets_data[col] = google_sheets_data[col].astype(str)
    excel_data[col] = excel_data[col].astype(str)

# Subset the dataframes to only include the columns to compare
google_sheets_data = google_sheets_data[columns_to_compare]
excel_data = excel_data[columns_to_compare]

# Merge the dataframes on the columns to compare, using an indicator to track where the rows come from
merged_data = pd.merge(google_sheets_data, excel_data,
                       how='left', indicator=True)

# Define a function to compare 'Style Name' based on fuzzy matching


def fuzzy_match(row):
    if row['_merge'] == 'both':
        google_row = google_sheets_data[google_sheets_data['Style No']
                                        == row['Style No']]
        if not google_row.empty:
            return fuzz.token_set_ratio(google_row['Style Name'].values[0], row['Style Name']) > 80
    return False


# Apply the function to each row in the merged data
merged_data['fuzzy_match'] = merged_data.apply(fuzzy_match, axis=1)

# Create a new dataframe 'updates' containing only the rows that don't match (based on exact match or fuzzy match)
updates = merged_data[(merged_data['_merge'] == 'left_only') | (
    merged_data['fuzzy_match'] == False)].copy()

updates.to_csv('updates.csv', index=False)
