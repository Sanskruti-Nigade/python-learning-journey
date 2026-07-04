import pandas as pd
import numpy as np

print("--- Assignment 4.1 ---")
# 1. Group by Category (sum and mean)
df4_1 = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], size=10),
    'Value': np.random.randint(10, 100, size=10)
})
grouped4_1 = df4_1.groupby('Category')['Value'].agg(['sum', 'mean'])
print(grouped4_1)

print("\n--- Assignment 4.2 ---")
# 2. Total sales by Category
df4_2 = pd.DataFrame({
    'Product': [f'Prod_{i}' for i in range(8)],
    'Category': np.random.choice(['Electronics', 'Clothing', 'Home'], size=8),
    'Sales': np.random.randint(100, 1000, size=8)
})
total_sales = df4_2.groupby('Category')['Sales'].sum()
print(total_sales)