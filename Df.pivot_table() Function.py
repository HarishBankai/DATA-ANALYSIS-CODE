import pandas as pd  
import numpy as np  

num = {
    'A': ['HAR', 'ATH', 'ATH', 'ABHI', 'ABHI', 'HAR', 'HAR', 'ATH'],
    'Region': ['one', 'zero', 'one', 'zero', 'one', 'zero', 'one', 'zero'],
    'Sales' : ['VK', 'SRT', 'VK', 'SRT', 'VK', 'SRT', 'VK', 'SRT'],
    'Amount': [100, 200, 300, 400, 500,600, 700, 800] ,
    'Unit': [10, 20, 30, 40, 50, 60, 70, 80]
}

df = pd.DataFrame(num)
print("Original DataFrame:")
print(df)

pivot_table_unit = pd.pivot_table(df, values = 'Unit', index='A', columns = 'Region', aggfunc='sum')
print("\nPivot Table (Sum of Unit):")
print(pivot_table_unit)

pivot_table_amount = pd.pivot_table(df, values = 'Amount', index='A', columns = 'Region', aggfunc='mean')
print("\nPivot Table (Avg of Amount):")
print(pivot_table_amount)

pivot_table_double = pd.pivot_table(df, values = 'Amount', index='A', columns = 'Region', aggfunc=['mean', 'sum'])
print("\nPivot Table (Avg & Sum of Amount):")
print(pivot_table_double)
