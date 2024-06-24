import preproc_db_train
import matplotlib.pyplot as plt

#filepath = 'example data db/example.json'
filepath = '../example data db/DB_Arnsdorf(Dresden)_2024-06-21-20-59-00.json'
mytrains = preproc_db_train.Train.from_json(filepath)

#for train in mytrains:
#        train.print_train()

# Extract departure times and convert them to datetime objects
departure_times = preproc_db_train.get_departure_times(mytrains)

# Count the number of departures per time unit (e.g., per hour)

# Get departure counts for the desired unit (hour, min, or day)
unit = "hour"  # Change to "min" or "day" as needed
departure_counts = preproc_db_train.get_departure_counts(unit, departure_times)

# Sort the counts by time
sorted_times = preproc_db_train.get_sorted_times(departure_counts)
sorted_counts = preproc_db_train.get_sorted_counts(departure_counts, sorted_times)

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(sorted_times, sorted_counts, marker='o')
plt.xlabel(f'Time ({unit})')
plt.ylabel('Number of Departures')
plt.title(f'Number of Trains Departing per {unit.capitalize()}')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()