import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

x_column = 'Q1 SALES'
y_column = 'Q3 SALES'

df.plot.scatter(x=x_column, y=y_column)

plt.title('Q1 SALES vs Q3 SALES')  
plt.xlabel('Q1 SALES')
plt.ylabel('Q3 SALES')
plt.show()