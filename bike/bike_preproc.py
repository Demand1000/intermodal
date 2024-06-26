import pandas as pd
import json
import os
from datetime import datetime


class bike:
    def read_bike_json_files_to_dataframe(folder_path):
        all_data = []

        for filename in os.listdir(folder_path):
            if filename.endswith(".json"):
                # Extract the timestamp from the file name
                timestamp_str = filename.split(".json")[0]
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d-%H-%M-%S")

                # Construct the full file path
                filepath = os.path.join(folder_path, filename)

                with open(filepath, "r") as file:
                    data = json.load(file)

                    # Extract relevant parts for DataFrame
                    places = data['countries'][0]['cities'][0]['places']

                    # Add the timestamp to each place data
                    for place in places:
                        place['time'] = timestamp

                    # Add all places data to the list
                    all_data.extend(places)

        # Convert the collected data to a DataFrame
        df = pd.json_normalize(all_data)

        return df

    def expand_bike_numbers(df):
        # Initialize an empty list to store the expanded data
        expanded_data = []

        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            lat = row['lat']
            lng = row['lng']
            name = row['name']
            time = row['time']

            # Iterate over each bike_number in the bike_numbers list
            for bike_number in row['bike_numbers']:
                # Create a new dictionary for each bike_number with additional features
                bike_data = {
                    'bike_number': bike_number,
                    'lat': lat,
                    'lng': lng,
                    'time': time,
                    'name': name,
                }

                # Append the bike_data to the expanded_data list
                expanded_data.append(bike_data)

        # Create a new DataFrame from the expanded_data list
        expanded_df = pd.DataFrame(expanded_data)

        return expanded_df