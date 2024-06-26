import folium
from datetime import datetime
import pandas as pd

# Initialize the map centered around the mean coordinates
def map_bike_locations(df):
    map_center = [df['lat'].mean(), df['lng'].mean()]
    mymap = folium.Map(location=map_center, zoom_start=12)

    # Add markers for each bike location
    for index, row in df.iterrows():
        folium.Marker(
            location=[row['lat'], row['lng']],
            popup=f"Bike Number: {row['bike_number']}<br>Time: {row['time'].strftime('%Y-%m-%d %H:%M:%S')}",
            icon=folium.Icon(color='blue', icon='bicycle', prefix='fa')
        ).add_to(mymap)

    # save the map
    mymap.save('bike_locations_map.html')