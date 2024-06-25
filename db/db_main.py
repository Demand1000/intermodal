import pandas as pd

import db.db_preproc
import db.db_plots

# Replace 'folder_JSON' with your actual folder path containing JSON files
folder_path = 'example data db'
df = db.db_preproc.Train.read_json_files_to_dataframe(folder_path)

df = db.db_preproc.Train.add_time_deltas(df=df)



# Set pandas options to display the full DataFrame
pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.max_rows', None)     # Display all rows
pd.set_option('display.max_colwidth', None) # Display full column width


df['Arrival Planned Count min'] = df.groupby('Arrival Planned')['Arrival Planned'].transform('count')

print(df.head())
print(df.info())
print(df)

db.db_plots.scatter_line_plot(df)
