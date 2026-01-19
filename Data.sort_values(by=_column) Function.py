import pandas as pd  
import numpy as np

# Create sample data for DataFrame
data = {
    'Batch_ID' : ['Maths', 'English', 'Science', 'History', 'Geography'] ,
    'Branch' : ['Z', 'B', 'C', 'A', 'E'] ,
    'S1' : [1, 3, 2, 5 , 4] ,
    'S2' : [10, 32, 23, 15 , 19] ,
    'S3' : [1, 12, 3, 25 , 19]
}

df = pd.DataFrame(data)

sorted_branch_s1 = df.sort_values(by=['Branch', 'S1'], ascending=[True, False])
print("Original DataFrame:")
print(df)

print("\nDataFrame sorted by 'Branch' ascending and 'S1' descending:")
print(sorted_branch_s1)

sorted_batch_s2 = df.sort_values(by=['Batch_ID', 'S2'], ascending=[True, False])
print("\nDataFrame sorted by 'Batch' ascending and 'S2' descending:")
print(sorted_batch_s2)

