import pandas as pd 
import numpy as np  
import matplotlib.pyplot as plt

date_range = pd.date_range(start="2006-01-01", end="2007-01-01", freq="h")
np.random.seed(0)
energy_date = np.random.uniform(100, 1000, len(date_range))

df = pd.DataFrame({'Timestamps':date_range, 'Energy_Consumption':energy_date})
df.set_index('Timestamps', inplace=True)

daily_consumption = df.resample('D').sum()
daily_consumption.columns = ["Daily_Total_kWh"]

weekly_comsumption = df.resample('W').mean()
weekly_comsumption.columns = ["Weekly_Avg_kWh"]

plt.figure(figsize=(14, 7))
plt.plot(daily_consumption.index, daily_consumption['Daily_Total_kWh'], label='Daily Total kWh', color='blue')
plt.title('Daily Energy Consumption')
plt.xlabel('Date')
plt.ylabel('Total kWh')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(14, 7))
plt.plot(weekly_comsumption.index, weekly_comsumption['Weekly_Avg_kWh'], label='Weekly Average kWh', color='orange')
plt.title('Weekly Average Energy Consumption')
plt.xlabel('Date')  
plt.ylabel('Average kWh')
plt.legend()    
plt.grid()
plt.show()