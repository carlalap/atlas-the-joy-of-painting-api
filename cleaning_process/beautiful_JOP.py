# script that clean and organized the content of the files /Data-Source
import pandas as pd

# reading files :
colors = pd.read_csv("../data_source/JOP_Colors_Used")
subject = pd.read_csv("../data_source/JOP_Subject_Matter")
dates = pd.read_fwf("../data_source/JOP_Episode_Dates.txt",
                    header=None, names=['raw_data'])

##### Start process 1 for cleaning data from the file JOP_Episode_Dates.txt  ##############

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
# Remove the 'raw_data' column.
dates.drop(columns=['raw_data'], inplace=True)
dates.drop(columns=['Description'], inplace=True)

# Save the result to a new CSV file.
# dates.to_csv('./clean_data/dates_clean.csv', index=False)

##### End process 1 ##############

##### Start process 2 for cleaning data from the file JOP_Colors_Used.csv ########

# Define and delimit the content by columns
colors.columns = ["ID", "Painting_index", "Img_src", "Title", "Season", "Episodes",
                  "Num_colors", "Youtube_src", "Colors", "Color_hex",
                  "Black_Gesso", "Bright_Red", "Burnt_Umber", "Cadmium_Yellow",
                  "Dark_Sienna", "Indian_Red", "Indian_Yellow", "Liquid_Black",
                  "Liquid_Clear", "Midnight_Black", "Phthalo_Blue", "Phthalo_Green",
                  "Prussian_Blue", "Sap_Green", "Titanium_White", "Van_Dyke_Brown",
                  "Yellow_Ochre", "Alizarin_Crimson"]

# Cleans data: brackets, quotes


def clean_string(x):
    if isinstance(x, str):
        return x.strip("[]").replace("'", "").replace('"', '')
    else:
        return x


# apply the cleaning function to all elements in the DataFrame
colors = colors.applymap(clean_string)
# Every word in Title start with Capital lleter
colors['Title'] = colors['Title'].str.lower().str.title()

# delete columns
colors = colors.drop(
    columns=colors.loc[:, 'Black_Gesso':'Alizarin_Crimson'])
# Save the result to a new CSV file.
# colors.to_csv("./clean_data/colors_clean.csv", index=False)


##### End process 2 ##############

##### Start process 3 for cleaning data from the file JOP_Subject_Matter.csv ########

# Set elements of first row with the first letter in Capital
subject.columns = subject.columns.str.title()

# add first column ID
subject.insert(0, 'ID', range(1, 1 + len(subject)))

# Give format to elements in column Title
subject['Title'] = subject['Title'].str.replace('"', '')
subject['Title'] = subject['Title'].str.lower().str.title()
# Creates a new column 'Subject' add the subject elements
subject['Subject'] = subject.loc[:, 'Apple_Frame':'Wood_Framed'].apply(
    lambda x: ', '.join(x.index[x == 1]), axis=1)
# delete columns
subject = subject.drop(columns=subject.loc[:, 'Apple_Frame':'Wood_Framed'])

# creates a new file
# subject.to_csv("./clean_data/subjects_clean.csv", index=False)

##### End process 3 ##############

##### Start of Merging Stage ##############

merged_jop = pd.merge(dates, pd.merge(subject, colors, on=[
    'ID', 'Title']), on=['ID', 'Title'])
# Save the result to a new CSV file.
merged_jop.to_csv("../data_source/beautiful_JOP.csv", index=False)

##### End Merging Stage ##############
