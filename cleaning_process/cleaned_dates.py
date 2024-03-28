# script that clean, organized the content of file txt: JOP_Episode_Dates.txt
import pandas as pd

# reading file data.csv
dates = pd.read_fwf("../data_source/JOP_Episode_Dates.txt",
                    header=None, names=['raw_data'])

# add column ID(PK)
dates['ID'] = dates.index + 1
# changing all values to string
dates['raw_data'] = dates['raw_data'].astype(str)
# Extract the "text" and add a new column Title
dates['Title'] = dates['raw_data'].str.extract(r'"(.*?)"')
# Every word in Title start with Capital lleter
dates['Title'] = dates['Title'].str.lower().str.title()
# Extract the month and date between parentheses
dates['Month'] = dates['raw_data'].str.extract(
    r'\((.*?)\)')[0].str.extract(r'(\w+)')
dates['Date'] = pd.to_datetime(dates['raw_data'].str.extract(
    r'\((.*?)\)')[0], format='%B %d, %Y').dt.strftime('%m-%d-%Y')

# Extract the description after the final parenthesis
dates['Description'] = dates['raw_data'].str.extract(r'\)(.*)')
# Remove columns.
dates.drop(columns=['Description'], inplace=True)
dates.drop(columns=['raw_data'], inplace=True)
# Save the result to a new CSV file.
dates.to_csv('./clean_data/dates_clean.csv', index=False)
