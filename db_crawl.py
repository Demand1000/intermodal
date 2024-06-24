from deutsche_bahn_api.api_authentication import ApiAuthentication
from deutsche_bahn_api.station_helper import StationHelper
from deutsche_bahn_api.timetable_helper import TimetableHelper
import json

import time
import os
from datetime import datetime, timedelta

# Set the working directory
os.chdir("C:/Users/Administrator/Documents/web_scarping/DB/dump")
#os.chdir("C:/Users/lukas/OneDrive/1.2 TU Dresden/4S Intermodal_Train/DB/dump")

# Fix execution times
stop_date_time = datetime.strptime("2024-06-30 23:59:00", "%Y-%m-%d %H:%M:%S")
now = datetime.now()
lapse_time = timedelta(seconds=60*60)  # crawl data every 60 seconds
exec_times = [stop_date_time - lapse_time * i for i in range(int((stop_date_time - now).total_seconds() // 60) + 1)]
exec_times = [et for et in exec_times if et >= datetime.strptime("2024-06-21 15:00:00", "%Y-%m-%d %H:%M:%S")]
exec_times.reverse()
print(exec_times)
wait_time_for_errors = 5  # wait time in seconds for retrying after errors


stations = {"Großenhain Cottb Bf":0,
            "Riesa":0,
            "Meißen":1,
            "Meißen Triebischtal":0,
            "Weinböhla Hp":0,
            "Neusörnewitz":0,
            "Radebeul-Weintraube":0,
            "Radebeul Ost":0,
            "Ottendorf-Okrilla Süd":0,
            "Königsbrück":0,
            "Freital-Potschappel":0,
            "Freital-Deuben":0,
            "Radeberg":0,
            "Tharandt":0,
            "Freital-Hainsberg":0,
            "Pulsnitz":0,
            "Großröhrsdorf":0,
            "Arnsdorf(Dresden)":0,
            "Kamenz(Sachs)":0,
            "Klingenberg-Colmnitz":0,
            "Heidenau":0,
            "Dürrröhrsdorf":0,
            "Pirna":0,
            "Bad Schandau":0,
            }


for exec_time in exec_times:
    exec_name = exec_time.strftime("%Y-%m-%d-%H-%M-%S")
    wait_time = (exec_time - datetime.now()).total_seconds()
    if wait_time > 0:
        print(f"\nWaiting {wait_time} seconds before next execution\n")
        time.sleep(wait_time)
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    for station_name, value in stations.items():
        # Download JSON file in a temporary file
        json_filename = f"C:/Users/Administrator/Documents/web_scarping/DB/dump/DB_{station_name.replace(' ', '_')}_{exec_name}.json"
        while True:
            try:
                # Use the API and download data
                api = ApiAuthentication("397f705001c520247dcc4eeac085b824", "cab57beb8ea4529dbb95791bc28d8680")
                success = api.test_credentials()

                if not success:
                    raise Exception("API authentication failed")

                station_helper = StationHelper()
                found_stations_by_name = station_helper.find_stations_by_name(station_name)
                station = found_stations_by_name[value]
                print(station)

                timetable_helper = TimetableHelper(station, api)

                # Get the current time
                now = datetime.now()

                # Subtract one hour from the current time
                four_hour_ago = now - timedelta(hours=4)

                # Extract the hour from one hour ago
                hour_four_hour_ago = four_hour_ago.hour

                trains_in_this_hour = timetable_helper.get_timetable(hour_four_hour_ago)  # like 18 o'clock

                trains_with_changes_in_this_hour = timetable_helper.get_timetable_changes(trains_in_this_hour)

                trains_data = []
                for train in trains_with_changes_in_this_hour:
                    train_info = {
                        "Train Type": str(train.train_type) if hasattr(train, 'train_type') else None,
                        "Train Line": str(train.train_line) if hasattr(train, 'train_line') else None,
                        "Train Number": str(train.train_number) if hasattr(train, 'train_number') else None,
                        "Platform": str(train.platform) if hasattr(train, 'platform') else None,
                        "Stations": str(train.stations) if hasattr(train, 'stations') else None,
                        "Arrival": str(train.arrival) if hasattr(train, 'arrival') else None,
                        "Changed Arrival": str(train.train_changes.arrival) if hasattr(train.train_changes, 'arrival') else None,
                        "Departure": str(train.departure) if hasattr(train, 'departure') else None,
                        "Changed Departure": str(train.train_changes.departure) if hasattr(train.train_changes, 'departure') else None
                    }
                    trains_data.append(train_info)

                with open(json_filename, 'w', encoding='utf-8') as f:
                    json.dump(trains_data, f, ensure_ascii=False, indent=4)

                print(f"Train information written to {json_filename}")
                break
            except Exception as e:
                print(f"\nEncountered a download error: {e}... Waiting {wait_time_for_errors} seconds before next try\n")
                time.sleep(wait_time_for_errors)
