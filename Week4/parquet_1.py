import pandas as pd

class parquet_file:
    def read_parquet_file(file_path):
        file_data = pd.read_parquet(file_path)
        print(file_data.head())

