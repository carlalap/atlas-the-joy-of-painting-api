import pandas as pd
import ast

# path the data file
data_source_2 = './Data_source/JOP_Episode_Dates'

# importing content of the data files
data_dates = pd.read_csv(data_source_2, header=None)

# Renaming columns to a common name 'Title' for consistency
data_dates.rename(columns={'Title': 'Title'}, inplace=True)

# Standardize content of common column to title case
data_dates['Title'] = dates['Title'].str.title()

# Convert the date string to a Pandas datetime object
date = pd.to_datetime(merged['Date'])

# Format the date in MySQL format "YYYY-MM-DD"
merged['Date'] = date.dt.strftime('%Y-%m-%d')

merged.to_csv('dates.csv')
