import pandas as pd  
import numpy as np

# Create sample data for first DataFrame
data1 = {
    'Batch_ID' : ['Maths', 'English', 'Science', 'History', 'Geography'] ,
    'S1' : [1, 2, 3, 5 , 9] ,
    'S2' : [10, 32, 23, 15 , 19] ,
    'S1' : [1, 2, 3, 5 , 9]
}

# Create sample data for second DataFrame
data2 = {
    'S4' : [20, 37, 27, 12 , 39] ,
    'S5' : [51, 72, 53, 65, 99]
}

# Create first DataFrame
df = pd.DataFrame(data1)
print("First DataFrame:")
print(df)

# Create second DataFrame
df1 = pd.DataFrame(data2)
print("Second DataFrame:")
print(df1)

# Merge dataframes on index (assuming matching indexes)
merged_df = pd.merge(df, df1, left_index=True, right_index=True)
print("Merged DataFrame:")
print(merged_df)