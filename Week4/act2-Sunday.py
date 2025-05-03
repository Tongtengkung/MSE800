import pandas as pd

parquet_df = pd.read_parquet('Sample_data_2.parquet')

num_features = len(parquet_df.columns)

print(f"Number of features: {num_features}")