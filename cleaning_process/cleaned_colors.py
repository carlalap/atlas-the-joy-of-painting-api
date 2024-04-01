# script that clean, organized the content of file csv: JOP_Colors_Used.csv
import pandas as pd

# Read the CSV file
colors = pd.read_csv("../data_source/JOP_Colors_Used")

# Define and delimit the content by columns
colors.columns = ["ID", "Painting_index", "Img_src", "Title", "Season", "Episode",
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
colors['Colors'] = colors['Colors'].str.replace('\r\n', '')
# delete columns from Black_Gesso - to Alizarin_Crimson
colors = colors.drop(
    columns=colors.loc[:, 'Black_Gesso':'Alizarin_Crimson'])
# Save the cleaned data to a new CSV file
colors.to_csv("./clean_data/colors_clean.csv", index=False)
