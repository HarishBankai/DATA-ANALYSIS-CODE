import pandas as pd  
import numpy as np

# Create sample data for first DataFrame
data1 = {
    'Batch_ID' : ['Maths', 'English', 'Science', 'History', 'Geography'] ,
    'S1' : [1, 2, 3, 5 , 9] ,
    'S2' : [10, 32, 23, 15 , 19] ,
    'S3' : [1, 2, 3, 5 , 9]
}

# Create sample data for second DataFrame
data2 = {
    'Batch_ID' : ['Maths', 'English', 'Science', 'History', 'Geography'] ,
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

# Concatenate DataFrames vertically while keeping all columns
concat_df = pd.concat([df, df1], axis=0)
print("Concatenated DataFrame:")
print(concat_df)