import pandas as pd

def load_and_inspect_data(filepath):
    # Load the CSV data
    data = pd.read_csv(filepath)
    
    # Print the first 5 rows
    print("First 5 rows of the data:")
    print(data.head())
    
    # Print the number of missing values in each column
    print("\nNumber of missing values in each column:")
    print(data.isnull().sum())

if __name__ == "__main__":
    # Path to the CSV file
    csv_filepath = 'data/health_data.csv'
    load_and_inspect_data(csv_filepath)
