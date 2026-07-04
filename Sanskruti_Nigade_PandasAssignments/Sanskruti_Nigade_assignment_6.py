import pandas as pd
import numpy as np

print("--- Assignment 6.1 ---")
# 1. Monthly mean resampling
dates6_1 = pd.date_range(start='2023-01-01', periods=100, freq='D')
df6_1 = pd.DataFrame(np.random.randint(1, 50, size=(100, 1)), index=dates6_1, columns=['Value'])
monthly_mean = df6_1.resample('ME').mean()
print("Monthly Mean:\n", monthly_mean)

print("\n--- Assignment 6.2 ---")
# 2. 7-day rolling mean
dates6_2 = pd.date_range(start='2021-01-01', end='2021-12-31', freq='D')
df6_2 = pd.DataFrame(np.random.randint(10, 100, size=(len(dates6_2), 1)), index=dates6_2, columns=['Value'])
df6_2['Rolling_7D'] = df6_2['Value'].rolling(window=7).mean()
print("Rolling Mean Sample (Head):\n", df6_2.head(10))