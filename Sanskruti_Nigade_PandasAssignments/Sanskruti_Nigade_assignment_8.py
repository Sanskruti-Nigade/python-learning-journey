import pandas as pd
import numpy as np

print("--- Assignment 8.1 ---")
# 1. Pivot Table: Sum of Value by Category and Date
df8_1 = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=6, freq='D').repeat(2),
    'Category': np.random.choice(['X', 'Y'], size=12),
    'Value': np.random.randint(10, 50, size=12)
})
pivot1 = df8_1.pivot_table(values='Value', index='Date', columns='Category', aggfunc='sum')
print(pivot1)

print("\n--- Assignment 8.2 ---")
# 2. Pivot Table: Mean Revenue by Quarter and Year
df8_2 = pd.DataFrame({
    'Year': [2021, 2021, 2022, 2022] * 2,
    'Quarter': ['Q1', 'Q2', 'Q1', 'Q2'] * 2,
    'Revenue': np.random.randint(1000, 5000, size=8)
})
pivot2 = df8_2.pivot_table(values='Revenue', index='Year', columns='Quarter', aggfunc='mean')
print(pivot2)