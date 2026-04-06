import pandas as pd


def load_data():
    """
    Load and clean health data from a CSV file.

    - Fill missing 'Steps' with the median value for that column.
    - Fill missing 'Sleep_Hours' with 7.0.
    - Fill missing 'Heart_Rate_bpm' with 68.
    - Fill missing values in other columns with their respective median.
    - Convert the 'Date' column to datetime objects.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # Load the CSV data
    data = pd.read_csv('data/health_data.csv')

    # Fill missing values
    # Fill missing 'Steps' with median
    if 'Steps' in data.columns:
        data['Steps'].fillna(data['Steps'].median(), inplace=True)
    
    # Fill missing 'Sleep_Hours' with 7.0
    if 'Sleep_Hours' in data.columns:
        data['Sleep_Hours'].fillna(7.0, inplace=True)

    # Fill missing 'Heart_Rate_bpm' with 68
    if 'Heart_Rate_bpm' in data.columns:
        data['Heart_Rate_bpm'].fillna(68, inplace=True)

    # Fill missing values in other columns with median
    for column in data.columns:
        if column not in ['Steps', 'Sleep_Hours', 'Heart_Rate_bpm', 'Date']:
            data[column].fillna(data[column].median(), inplace=True)

    # Convert 'Date' column to datetime
    if 'Date' in data.columns:
        data['Date'] = pd.to_datetime(data['Date'])

    return data


def calculate_recovery_score(df):
    """
    Calculate and add a 'Recovery_score' column to the dataframe.

    The Recovery_score is based on 'Sleep_Hours', 'Heart_Rate_bpm', and 'Steps':
    - Good sleep (7+ hours) significantly improves the score.
    - Poor sleep (less than 6 hours) heavily reduces the score.
    - Lower heart rate improves recovery.
    - Very high activity (steps) might reduce recovery slightly due to strain.

    The final Recovery_score ranges from 0 to 100.

    Args:
        df (pd.DataFrame): DataFrame containing the health data.

    Returns:
        pd.DataFrame: DataFrame with 'Recovery_score' column added.
    """
    # Define baseline scores
    baseline_sleep_score = 50
    baseline_heart_rate_score = 30
    baseline_activity_score = 20

    # Initialize Recovery_score to 0
    df['Recovery_score'] = 0

    # Calculate scores based on Sleep_Hours
    df.loc[df['Sleep_Hours'] >= 7, 'Recovery_score'] += baseline_sleep_score  # Good sleep
    df.loc[df['Sleep_Hours'] < 6, 'Recovery_score'] -= 20  # Poor sleep penalty

    # Calculate scores based on Heart_Rate_bpm
    df['Recovery_score'] += baseline_heart_rate_score - (df['Heart_Rate_bpm'] - 50) * 0.3

    # Calculate scores based on Steps
    df.loc[(df['Steps'] > 8000) & (df['Steps'] <= 12000), 'Recovery_score'] += baseline_activity_score  # Active
    df.loc[df['Steps'] > 12000, 'Recovery_score'] -= 10  # Over-exercise penalty

    # Ensure Recovery_score is within 0 to 100
    df['Recovery_score'] = df['Recovery_score'].clip(0, 100)

    return df

