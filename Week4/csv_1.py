import pandas as pd

class csv_file:
    def read_csv_file(file_path):
        file_data = pd.read_csv(file_path)
        print(file_data.head())
