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