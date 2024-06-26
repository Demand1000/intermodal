import pandas as pd

import train.train_preproc
import train.train_plots

# Replace 'folder_JSON' with your actual folder path containing JSON files
folder_path = 'example_data_train'
df = train.train_preproc.Train.read_json_files_to_dataframe(folder_path)

df = train.train_preproc.Train.add_time_deltas(df=df)



# Set pandas options to display the full DataFrame
pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.max_rows', None)     # Display all rows
pd.set_option('display.max_colwidth', None) # Display full column width


df['Arrival Planned Count min'] = df.groupby('Arrival Planned')['Arrival Planned'].transform('count')
df['Arrival Changed Count min'] = df.groupby('Arrival Changed')['Arrival Changed'].transform('count')

print(df.head())
print(df.info())
print(df)

#train.db_plots.scatter_line_plot(df=df, input_station="Arnsdorf(Dresden)")
train.train_plots.scatter_line_plot(df=df, input_station="Weinböhla_Hp")

