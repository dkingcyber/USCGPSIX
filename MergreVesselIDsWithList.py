# This script merges the Vessel IDs with the Vessel Names from the provided CSV files.

import pandas as pd
import datetime

# Load the spreadsheets
# Update the file paths to where your CSV files are located
vessels_data = pd.read_csv('')    # This file should have the Vessel Names and IDs
activity_data = pd.read_csv('')   # This file should have the activities with Vessel IDs

merged_data = pd.merge(activity_data, vessels_data[['VesselId', 'Vessel Name']], on='VesselId', how='left')

cols = merged_data.columns.tolist()
vessel_name_index = cols.index('Vessel Name')
cols = [cols[vessel_name_index]] + cols[:vessel_name_index] + cols[vessel_name_index+1:]
merged_data = merged_data[cols]

# Save the merged data to a new CSV file with date
date = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
merged_data.to_csv(f'merged_file{date}.csv', index=False)
print('Merged data saved to file.')