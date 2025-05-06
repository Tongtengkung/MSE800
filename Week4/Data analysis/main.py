import pandas as pd

# Specify the path to your CSV file
file_path = r'C:\Users\norra\OneDrive\Documents\GitHub\MSE800\Week4\Data analysis\mydata.csv'  # Use a raw string
# OR
# file_path = 'C:/Users/norra/OneDrive/Documents/GitHub/MSE800/Week4/Data analysis/mydata.csv'  # Use forward slashes


try:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Basic Summary Statistics
    print("Summary Statistics:")
    print(df['STATS_VALUE'].describe())
    print("\n")

    # Group by Year and calculate the mean
    print("Average Stats Value per Year:")
    print(df.groupby('YEAR')['STATS_VALUE'].mean())
    print("\n")

    #Find the month with the highest stats value
    max_stats = df['STATS_VALUE'].max()
    month_with_max_stats = df[df['STATS_VALUE'] == max_stats]['PERIOD'].iloc[0]
    year_with_max_stats = df[df['STATS_VALUE'] == max_stats]['YEAR'].iloc[0]

    print(f"Month with the Highest Stats Value: {month_with_max_stats} in {year_with_max_stats} with a value of {max_stats}")
    print("\n")

    # Find the month with the lowest stats value
    min_stats = df['STATS_VALUE'].min()
    month_with_min_stats = df[df['STATS_VALUE'] == min_stats]['PERIOD'].iloc[0]
    year_with_min_stats = df[df['STATS_VALUE'] == min_stats]['YEAR'].iloc[0]

    print(f"Month with the Lowest Stats Value: {month_with_min_stats} in {year_with_max_stats} with a value of {min_stats}")


except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")