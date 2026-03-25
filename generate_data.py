import pandas as pd
import numpy as np
from numpy.random import default_rng
from scipy.stats import norm

# Set the random seed for reproducibility
rng = default_rng(42)

# Date range for 365 days starting from 2025-01-01
dates = pd.date_range(start="2025-01-01", periods=365, freq='D')

# Generate synthetic data using normal distributions with realistic ranges
steps = np.clip(rng.normal(loc=8500, scale=2500, size=365), 3000, 18000)
sleep_hours = np.clip(rng.normal(loc=7, scale=1.5, size=365), 4.5, 9.5)
heart_rate_bpm = np.clip(rng.normal(loc=68, scale=10, size=365), 48, 110)
calories_burned = np.clip(rng.normal(loc=3000, scale=600, size=365), 1800, 4200)
active_minutes = np.clip(rng.normal(loc=100, scale=40, size=365), 20, 180)

# Introduce 5% NaN values randomly across each column
def introduce_nan(data, nan_ratio=0.05):
    nan_indices = rng.choice(len(data), int(len(data) * nan_ratio), replace=False)
    data[nan_indices] = np.nan
    return data

steps = introduce_nan(steps)
sleep_hours = introduce_nan(sleep_hours)
heart_rate_bpm = introduce_nan(heart_rate_bpm)
calories_burned = introduce_nan(calories_burned)
active_minutes = introduce_nan(active_minutes)

# Create the DataFrame
fitness_data = pd.DataFrame({
    'Date': dates,
    'Steps': steps,
    'Sleep_Hours': sleep_hours,
    'Heart_Rate_BPM': heart_rate_bpm,
    'Calories_Burned': calories_burned,
    'Active_Minutes': active_minutes
})

# Save the dataset to a CSV file
fitness_data.to_csv('fitness_data.csv', index=False)

def main():
    print("Generated fitness data for 365 days and saved to fitness_data.csv")

if __name__ == "__main__":
    main()
