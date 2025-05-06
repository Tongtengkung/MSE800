import pandas as pd

data_file = 'iris.data'                                                                     # or full path if in a different directory

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']    # Load the data assuming no headers in the data file

iris_df = pd.read_csv(data_file, header=None, names=column_names)

flower_names = iris_df['species'].unique()                                                  # Get unique flower names from the 'species' column    

print("Flower names in the dataset:")                                                       # Print the unique flower names                 
for name in flower_names:
    print(name)