from pathlib import Path
import pandas as pd
from zipfile import ZipFile

data_dir = Path('data')
data_dir.mkdir(exist_ok = True)
file_path = data_dir / Path('PPD2_Jan_21_2022.zip')
dest_path = file_path

# Unzipping and getting the CV file.
with ZipFile(dest_path, 'r') as my_zip:
    
    csv_filename = 'PPD2_Jan_21_2022.csv'

    my_zip.extract(csv_filename, path='temp')
    csv_path = Path('temp') / csv_filename
    df = pd.read_csv(csv_path)

df = df[df['donor'] != '2.950000048']
df = df.dropna(subset=['donor'])

first_33_columns = df.iloc[:, :33]
last_columns = df.iloc[:, -20:]

# Concatenate the selected columns into a new DataFrame
all_aid = pd.concat([first_33_columns, last_columns], axis=1)

# Select the last row from the original DataFrame

unique_donors = df['donor'].unique()

# Create a list to store dataset names
dataset_names = []

# Create DataFrames for each donor with specific names
for donor in unique_donors:
    # Create a DataFrame with a specific name based on the donor
    donor_df = df[df['donor'] == donor].copy()
    
    # Define the naming convention (replace spaces with underscores and add a prefix)
    # donor_name = donor # Convert spaces to underscores and lowercase
    dataset_name = f"{donor}_df"
    
    # Assign the DataFrame to a variable with the specified name
    globals()[dataset_name] = donor_df
    
    # Add the dataset name to the list
    dataset_names.append(dataset_name)

# Print the list of dataset names
print("List of dataset names:")
print(dataset_names)
