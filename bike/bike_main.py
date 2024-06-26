#usefull string
#{"uid":405231635,"lat":51.043996,"lng":13.703084,"bike":true,"name":"BIKE 930589","address":null,"spot":false,"number":0,"booked_bikes":0,"bikes":1,"bikes_available_to_rent":1,"bike_racks":0,"free_racks":0,"special_racks":0,"free_special_racks":0,"maintenance":false,"terminal_type":"","bike_list":[{"number":"930589","bike_type":196,"lock_types":["frame_lock","dls"],"active":true,"state":"ok","electric_lock":true,"boardcomputer":7551052515,"pedelec_battery":null,"battery_pack":null}],"bike_numbers":["930589"],"bike_types":{"196":1},"place_type":"12","rack_locks":false}

import pandas as pd
import json
import os
from datetime import datetime

import bike_preproc

# Set pandas options to display the full DataFrame
pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.max_rows', None)     # Display all rows
pd.set_option('display.max_colwidth', None) # Display full column width


folder_path = 'example_data_bike'
bike_df = bike_preproc.bike.read_bike_json_files_to_dataframe(folder_path=folder_path)

# Keep only the specified columns
columns_to_keep = ['uid', 'lat', 'lng', 'bike', 'name', 'terminal_type', 'bike_numbers', 'time']
bike_df = bike_df[columns_to_keep]


# Display the DataFrame
print(bike_df)
print(bike_df.info())
