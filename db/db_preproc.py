import json
import os
import pandas as pd


class Train:
    def __init__(self, data):
        self.train_type = data.get("Train Type")
        self.train_line = data.get("Train Line")
        self.train_number = data.get("Train Number")
        self.platform = data.get("Platform")
        self.stations = data.get("Stations")
        self.arrival_planned = data.get("Arrival")
        self.arrival_changed = data.get("Changed Arrival")
        self.departure_planned = data.get("Departure")
        self.departure_changed = data.get("Changed Departure")

    def print_train(self):
        print("###")
        print("train type:", self.train_type)
        print("train line:", self.train_line)
        print("train number:", self.train_number)
        print("platform:", self.platform)
        print("stations:", self.stations)
        print("arrival_planned:", self.arrival_planned)
        print("arrival_changed:", self.arrival_changed)
        print("departure_planned:", self.departure_planned)
        print("departure_changed:", self.departure_changed)

    def to_dict(self):
        return {
            "Train Type": self.train_type,
            "Train Line": self.train_line,
            "Train Number": self.train_number,
            "Platform": self.platform,
            "Stations": self.stations,
            "Arrival Planned": pd.to_datetime(self.arrival_planned, format="%y%m%d%H%M"), #change date columns to date format
            "Arrival Changed": pd.to_datetime(self.arrival_changed, format="%y%m%d%H%M"),
            "Departure Planned": pd.to_datetime(self.departure_planned, format="%y%m%d%H%M"),
            "Departure Changed": pd.to_datetime(self.departure_changed, format="%y%m%d%H%M")
        }


    def read_json_files_to_dataframe(folder_path):
        all_data = []
        for filename in os.listdir(folder_path):
            if filename.endswith(".json"):
                filepath = os.path.join(folder_path, filename)
                with open(filepath, "r") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        for item in data:
                            train_instance = Train(item)
                            all_data.append(train_instance.to_dict())
                    else:
                        train_instance = Train(data)
                        all_data.append(train_instance.to_dict())
        return pd.DataFrame(all_data)


    def add_time_deltas(df):
        #TODO uses dropNA -> check if those trains where on time, or canceled
        df['Arrival Delta'] = ((df['Arrival Changed'] - df['Arrival Planned']).dt.total_seconds() / 60).dropna(
            ).round(decimals=0).astype(int)
        df['Departure Delta'] = ((df['Departure Changed'] - df['Departure Planned']).dt.total_seconds() / 60).dropna(
            ).round(decimals=0).astype(int)
        return df

    @classmethod
    def from_json(cls, filepath):
        # Open and read the json file
        with open(filepath, "r") as f:
            data = json.load(f)
            # Check if the data is a list
            if isinstance(data, list):
                return [cls(item) for item in data]
            else:
                return cls(data)
