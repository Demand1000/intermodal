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
df_bike__stations_and_single_bikes = bike_preproc.bike.read_bike_json_files_to_dataframe(folder_path=folder_path)

# Keep only the specified columns
columns_to_keep = ['uid', 'lat', 'lng', 'bike', 'name', 'terminal_type', 'bike_numbers', 'time']
df_bike__stations_and_single_bikes = df_bike__stations_and_single_bikes[columns_to_keep]


def get_filter_dataframe(df):
    # lat lng
    #Kamenz as northern bound 51.16 (and 14.6)
    #Dippoldiswalde as southern bound 50.54 (and 13.4)
    #Meißen as western bound (51.10 and) 13.29
    #Stadt Wehlen as eastern bound(50.57 and) 14.2

    #latitude and longitude ranges
    lat_min, lat_max = 50.54, 51.16
    lng_min, lng_max = 13.29, 14.2

    # Apply the filter condition
    filtered_df = df[
        (df['lat'] >= lat_min) & (df['lat'] <= lat_max) &
        (df['lng'] >= lng_min) & (df['lng'] <= lng_max)
        ]

    return filtered_df

df_bike__stations_and_single_bikes = get_filter_dataframe(df_bike__stations_and_single_bikes)

# Display the DataFrame
#print(bike_df)
#print(bike_df.info())


#I want now for every bike_number in bike_numbers row, that has the additional features: time, lat, lng, name
df_bike__bikes_per_bike_number = bike_preproc.bike.expand_bike_numbers(df=df_bike__stations_and_single_bikes)

# Display the expanded DataFrame
print(df_bike__bikes_per_bike_number)
print(df_bike__bikes_per_bike_number.info())
print(df_bike__bikes_per_bike_number.describe())

import folium
from datetime import datetime
import pandas as pd

# Initialize the map centered around the mean coordinates
map_center = [df_bike__bikes_per_bike_number['lat'].mean(), df_bike__bikes_per_bike_number['lng'].mean()]
mymap = folium.Map(location=map_center, zoom_start=12)

# Add markers for each bike location
for index, row in df_bike__bikes_per_bike_number.iterrows():
    folium.Marker(
        location=[row['lat'], row['lng']],
        popup=f"Bike Number: {row['bike_number']}<br>Time: {row['time'].strftime('%Y-%m-%d %H:%M:%S')}",
        icon=folium.Icon(color='blue', icon='bicycle', prefix='fa')
    ).add_to(mymap)

# save the map
mymap.save('bike_locations_map.html')

#from current location to origin-destination-flow
#store all bike numbers
#If one bike number disappears it is rented.
#If is appears again, than:
    #take start time and location (last before it disappeared)
    #take end time and location (when it appeared again)
#print that on the map.
#show bar plot of air distance travelled, renting time, an the respective average speed
#delete, where average speed is below 3km/h (walking speed) --> ask sebastian about official criteria, either a near round trip or pushed while walking


#Now I need a list with all geo locations of the park&ride places and their respective train stations
#Define e.g. 200m cube around this point and just show those bicycles