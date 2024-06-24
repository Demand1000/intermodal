import json

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

filepath = 'example data db/example.json'
mytrains = Train.from_json(filepath)

for train in mytrains:
        train.print_train()
