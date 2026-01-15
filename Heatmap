import pandas as pd
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt


#Generate a sample data

data = {
    "S1" : np.random.rand(10) ,
    "S2" : np.random.rand(10) * 3 ,
    "S3" : np.random.rand(10) * 2 ,
    "S4" : np.random.rand(10) * 6 ,
    "S5" : np.random.rand(10) * 4 
}

df = pd.DataFrame(data)

print(df)

plt.figure(figsize=(10,7))
sns.heatmap(df.corr(), annot = True, cmap='coolwarm')
plt.title("Coreelation of Matrix using Heatmap")
plt.show()