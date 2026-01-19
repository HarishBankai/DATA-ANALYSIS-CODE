import pandas as pd  
import numpy as np  

# 1.Creation of the Sample Data: A time series dataset containing 100 days' worth of random sales data is created.
np.random.seed(100)

# Create date range from 2006-09-04 to 200 days later
dates = pd.date_range(start = '2006-09-04', periods = 200)

# Create dataframe with random sales data
data = {'Date': dates , 'Sales': np.random.randint(99, 198, size = 200)}
df = pd.DataFrame(data)

# Set Date column as index and ensure it's sorted
df.set_index('Date', inplace = True)

# Calculate the rolling mean with a window size of 7
# 2.Moving Average for 7 days: dff'Sales'.rolling (window=7).mean() provides a smoothed trend by calculating the moving average of sales figures over the previous seven days.
df['7-day AVG'] = df['Sales'].rolling(window=7).mean()

# 3.df['Sales'] is the 7-day rolling standard deviation.rolling (window=7).Finding stable and unstable times can be aided by using std(), which computes the volatility (standard deviation) in sales over the previous seven days.
df['7-day STD'] = df['Sales'].rolling(window=7).std()

# Show first 15 rows of dataframe with calculations
print("Sample Data with 7-day Rolling Mean and STD:")
print(df.head(15))




