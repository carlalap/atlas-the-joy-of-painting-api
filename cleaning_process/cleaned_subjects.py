# script that clean and organized the content of file csv: JOP_Subject_Matter.csv
import pandas as pd
import ast

# Read the CSV file
subject = pd.read_csv("../data_source/JOP_Subject_Matter")

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
subject.to_csv("./clean_data/subjects_clean.csv", index=False)
