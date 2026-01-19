import pandas as pd  
import numpy as np  

data = {
    "Product" : ['A', 'B', 'C'],
    "Q1 SALES" : [100, 327, 257],
    "Q2 SALES" : [150, 285, 350],
    "Q3 SALES" : [300, 157, 400],
    "Q4 SALES" : [275, 455, 287]
}

df = pd.DataFrame(data)
print("Original DataFrame(Wide Format): ")
print(df)

df_melted = pd.melt(
    df,  
    id_vars=['Product'],  # Keep Product as identifier
    value_vars=[
        'Q1 SALES', 
        'Q2 SALES',
        'Q3 SALES',
        'Q4 SALES'
    ],
    var_name='Quarter',
    value_name='Sales')
print("\nMelted DataFrame(Long Format): ")
print(df_melted)