import pandas as pd
import ast

# path the data file
data_source_1 = './Data_source/JOP_Colors_Used'
data_source_2 = './Data_source/JOP_Episode_Dates'
data_source_3 = './Data_source/JOP_Subject_Matter'

# importing content of the data files
data_colors = pd.read_csv(data_source_1)
data_dates = pd.read_csv(data_source_2, header=None)
data_subject = pd.read_csv(data_source_3)


# Split data, only after first occurrence of '" '
data_dates[['Title', 'Date']] = data_dates[0].str.extract(r'"(.*?)" \((.*?)\)')

# Add  separate column for month
data_dates['Month'] = data_dates['Date'].str.extract(r'(\w+) \d+, \d+')

# Remove extra column
del data_dates[0]
# Remove any additional text after the date
data_dates['Date'] = data_dates['Date'].str.split('(').str[0]

# Remove unnamed column
del data_colors['Unnamed: 0']

# Renaming columns to a common name 'Title' for consistency
data_dates.rename(columns={'Title': 'Title'}, inplace=True)
data_subject.rename(columns={'TITLE': 'Title'}, inplace=True)
data_colors.rename(columns={'painting_title': 'Title'}, inplace=True)

# Standardize content of common column to title case
data_dates['Title'] = data_dates['Title'].str.title()
data_subject['Title'] = data_subject['Title'].str.title()
data_colors['Title'] = data_colors['Title'].str.title()

# Remove quotes from 'Title' for consistency before merging
data_subject['Title'] = data_subject['Title'].str.replace('"', '')

# Merging based on the standardized common column 'Title'
merged = pd.merge(data_dates, data_colors, on='Title')
merged = pd.merge(merged, datas_subject, on='Title')

# Convert string representation of lists to actual lists
merged['colors'] = merged['colors'].apply(ast.literal_eval)

# Replace the '\r\n' in the lists
merged['colors'] = merged['colors'].apply(
    lambda x: [color.replace('\r\n', '') for color in x])

# Save to CSV
merged.to_csv('joy_of_painting.csv')
merged.columns
