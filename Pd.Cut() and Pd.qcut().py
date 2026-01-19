# Necessary Libraries
import pandas as pd
import numpy as np

# Generate a sample dataset
np.random.seed(0)
n = 1000
data = {
    'Customer': range(1, n + 1),
    'Age': np.random.randint(20, 60, n),
    'Annual_Spend': np.random.uniform(600, 20000, n),
    'Purchase_Frequency': np.random.poisson(20, n)
}
df = pd.DataFrame(data)

# Step 1
age_bins = [12, 30, 45, 70, 80]
age_labels = ['18-29', '30-44', '45-59', '60-70']
df['Age_Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

# Step 2
df['Spend_Segment'] = pd.qcut(df['Annual_Spend'], q=4, labels=['Low', 'Medium', 'High', 'Very High']) \

segment_analysis = df.groupby(['Age_Group', 'Spend_Segment']).agg({
    'Purchase_Frequency': ['mean', 'median', 'std'],
    'Annual_Spend': 'mean',
    'Customer': 'count'
}).reset_index()

# Renaming columns
segment_analysis.columns = ['Age_Group', 'Spend_Segment', 'Avg_Purchase_Freq', 'Median_Purchase_Freq', 'Purchase_Freq_Std', 'Avg_Annual_Spend', 'Customer_Count']

# Sort by Spend Segment and Age Group
segment_analysis = segment_analysis.sort_values(by=['Spend_Segment', 'Age_Group'])

print("Customer Segmentation Analysis:")
print(segment_analysis)