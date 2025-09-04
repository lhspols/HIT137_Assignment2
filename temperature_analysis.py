import pandas as pd
import os
import glob
import numpy as np

def load_all_data(folder="temperatures"):
    all_files = glob.glob(os.path.join(folder, "*.csv"))
    df_list = []
    for file in all_files:
        df = pd.read_csv(file)
        df_list.append(df)
    combined = pd.concat(df_list, ignore_index=True)
    return combined

def calculate_seasonal_average(df):
    month_to_season = {
        "January": "Summer", "February": "Summer", "December": "Summer",
        "March": "Autumn", "April": "Autumn", "May": "Autumn",
        "June": "Winter", "July": "Winter", "August": "Winter",
        "September": "Spring", "October": "Spring", "November": "Spring"
    }

    temp_cols = df.columns[4:]  # Ignore first 4 columns
    seasonal_sums = {"Summer": [], "Autumn": [], "Winter": [], "Spring": []}

    for month in temp_cols:
        season = month_to_season[month]
        seasonal_sums[season].append(df[month])

    seasonal_avg = {}
    for season, values in seasonal_sums.items():
        # Combine all values, ignore NaN
        all_vals = pd.concat(values, axis=0)
        seasonal_avg[season] = all_vals.mean()

    with open("average_temp.txt", "w") as f:
        for season, temp in seasonal_avg.items():
            f.write(f"{season}: {temp:.1f}°C\n")

def calculate_largest_temp_range(df):
    temp_cols = df.columns[4:]
    df["Max"] = df[temp_cols].max(axis=1)
    df["Min"] = df[temp_cols].min(axis=1)
    df["Range"] = df["Max"] - df["Min"]
    max_range = df["Range"].max()
    stations = df[df["Range"] == max_range]["STATION_NAME"].tolist()

    with open("largest_temp_range_station.txt", "w") as f:
        for station in stations:
            max_val = df[df["STATION_NAME"] == station]["Max"].values[0]
            min_val = df[df["STATION_NAME"] == station]["Min"].values[0]
            f.write(f"Station {station}: Range {max_range:.1f}°C (Max: {max_val:.1f}°C, Min: {min_val:.1f}°C)\n")

def calculate_temperature_stability(df):
    temp_cols = df.columns[4:]
    df["StdDev"] = df[temp_cols].std(axis=1)
    min_std = df["StdDev"].min()
    max_std = df["StdDev"].max()
    stable_stations = df[df["StdDev"] == min_std]["STATION_NAME"].tolist()
    variable_stations = df[df["StdDev"] == max_std]["STATION_NAME"].tolist()

    with open("temperature_stability_stations.txt", "w") as f:
        for station in stable_stations:
            f.write(f"Most Stable: Station {station}: StdDev {min_std:.1f}°C\n")
        for station in variable_stations:
            f.write(f"Most Variable: Station {station}: StdDev {max_std:.1f}°C\n")

def main():
    df = load_all_data("temperatures")
    calculate_seasonal_average(df)
    calculate_largest_temp_range(df)
    calculate_temperature_stability(df)
    print("Temperature analysis complete. Results saved to text files.")

if __name__ == "__main__":
    main()
