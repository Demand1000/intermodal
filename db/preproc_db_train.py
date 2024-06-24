import json
import datetime
from collections import Counter

class Train:
    def __init__(self, data):
        self.train_type = data.get("Train Type")
        self.train_line = data.get("Train Line")
        self.train_number = data.get("Train Number")
        self.platform = data.get("Platform")
        self.stations = data.get("Stations")
        self.arrival = data.get("Arrival")
        self.changed_arrival = data.get("Changed Arrival")
        self.departure = data.get("Departure")
        self.changed_departure = data.get("Changed Departure")

    def print_train(self):
        print("###")
        print("train type:", self.train_type)
        print("train line:", self.train_line)
        print("train number:", self.train_number)
        print("platform:", self.platform)
        print("stations:", self.stations)
        print("arrival:", self.arrival)
        print("changed arrival:", self.changed_arrival)
        print("departure:", self.departure)
        print("changed departure:", self.changed_departure)


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


# Function to convert the departure time to a datetime object
def convert_departure_time(departure):
    return datetime.datetime.strptime(departure, "%d%m%y%H%M")

#for train in mytrains:
#        train.print_train()

# Extract departure times and convert them to datetime objects
def get_departure_times(mytrains):
    departure_times = [convert_departure_time(train.departure) for train in mytrains]
    return departure_times

# Count the number of departures per time unit (e.g., per hour)
def get_departure_counts(unit, departure_times):
    departure_counts = {}
    for time in departure_times:
        if unit == "hour":
            time_str = time.strftime("%Y-%m-%d %H:00")
        elif unit == "min":
            time_str = time.strftime("%Y-%m-%d %H:%M")
        elif unit == "day":
            time_str = time.strftime("%Y-%m-%d")
        if time_str not in departure_counts:
            departure_counts[time_str] = 0
        departure_counts[time_str] += 1
    return departure_counts


# Sort the counts by time
def get_sorted_times(departure_counts):
    sorted_times = sorted(departure_counts.keys())
    return sorted_times

def get_sorted_counts(departure_counts, sorted_times ):
    sorted_counts = [departure_counts[time] for time in sorted_times]
    return sorted_counts