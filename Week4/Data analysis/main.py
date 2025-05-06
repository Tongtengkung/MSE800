import pandas as pd


file_path = r'C:\Users\norra\OneDrive\Documents\GitHub\MSE800\Week4\Data analysis\mydata.csv' 

try:
    df = pd.read_csv(file_path)                                                     # Read the CSV file into a pandas DataFrame

    print("Summary Statistics:")                                                    # Basic Summary Statistics
    print(df['STATS_VALUE'].describe())
    print("\n")

    print("Average Stats Value per Year:")                                          # Average Stats Value per Year
    print(df.groupby('YEAR')['STATS_VALUE'].mean())
    print("\n")

    max_stats = df['STATS_VALUE'].max()                                             # Find the maximum stats value
    month_with_max_stats = df[df['STATS_VALUE'] == max_stats]['PERIOD'].iloc[0]
    year_with_max_stats = df[df['STATS_VALUE'] == max_stats]['YEAR'].iloc[0]

    print(f"Month with the Highest Stats Value: {month_with_max_stats} in {year_with_max_stats} with a value of {max_stats}")
    print("\n")

    
    min_stats = df['STATS_VALUE'].min()                                             # Find the minimum stats value
    month_with_min_stats = df[df['STATS_VALUE'] == min_stats]['PERIOD'].iloc[0]
    year_with_min_stats = df[df['STATS_VALUE'] == min_stats]['YEAR'].iloc[0]

    print(f"Month with the Lowest Stats Value: {month_with_min_stats} in {year_with_max_stats} with a value of {min_stats}")


except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")