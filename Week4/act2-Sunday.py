import pandas as pd

parquet_df = pd.read_parquet('Sample_data_2.parquet')               # Read the Parquet file into a DataFrame    

print(parquet_df.head())                                            # Display the first few rows of the DataFrame                               
num_features = len(parquet_df.columns)                              # Count the number of features (columns) in the DataFrame       

print(f"Number of features: {num_features}")                        # Print the number of features (columns) in the DataFrame